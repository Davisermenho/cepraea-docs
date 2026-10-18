#!/usr/bin/env python3
"""Stop-hook continuation: preserve, open/reuse PR, reconcile reviews/checks, gated merge.

Each Stop is a single reconciliation tick. Pending checks/reviews are retried at
the next Stop; they are never interpreted as approval.
"""
import os
from pathlib import Path

from espaut.acceptance import verify_acceptance
from espaut.checks import query_checks
from espaut.events import log_event
from espaut.gh_ops import pr_view_json, run_gh
from espaut.git_ops import current_branch, has_incomplete_operation, head_sha, remote_head_sha, worktree_status
from espaut.governance import evaluate_merge_eligibility
from espaut.preservation import push_and_verify, run_preservation
from espaut.pullrequest import create_or_reuse_pr, query_pr_state, update_task_pr
from espaut.review import collect_reviews, extract_pendencies
from espaut.store import load_config, read_json, write_json


def checkpoint(store, task_id, status, **details):
    report = {"task_id": task_id, "status": status, **details}
    write_json(store / "cache" / f"stop-cycle-{task_id}.json", report)
    log_event(store, "stop_cycle", task_id=task_id, outcome=status,
              detail=str(details.get("reason", ""))[:200])
    if status in {"review_pending", "merge_pending", "pr_pending"}:
        # Detached continuation is activated only by a project's auto_merge
        # policy; the worker checks a per-task lock before doing any work.
        try:
            from espaut.stop_worker import launch_worker
            launched = launch_worker(store, task_id, str(store.parent))
            if launched:
                report["followup_spawned"] = True
                write_json(store / "cache" / f"stop-cycle-{task_id}.json", report)
        except (OSError, ValueError, RuntimeError) as exc:
            report["followup_error"] = type(exc).__name__
            write_json(store / "cache" / f"stop-cycle-{task_id}.json", report)
    return report


def human_approved(task, decisions, sha):
    return any(
        d.get("task_id") == task["task_id"]
        and d.get("decision_type") == "merge_authorization"
        and d.get("decision_value") == "approved"
        and bool(d.get("authority"))
        and (d.get("scope") == sha or d.get("revision") == sha)
        for d in decisions
    )


def run_stop_cycle(store: Path, task: dict, *, cwd: str, preserve_changes=True):
    """Execute only explicitly authorized steps, never accept unknown as PASS."""
    task_id = task["task_id"]
    cfg = load_config(store)
    branch = current_branch(cwd)
    if not branch or branch in ("main", "master") or branch != task.get("branch_name"):
        return checkpoint(store, task_id, "blocked", reason="wrong or protected branch")
    if has_incomplete_operation(cwd):
        return checkpoint(store, task_id, "blocked", reason="unfinished Git operation")
    patterns = cfg.get("eligible_patterns")
    if cfg.get("auto_commit") is not True or not isinstance(patterns, list) or not patterns:
        return checkpoint(store, task_id, "monitor_only", reason="explicit project opt-in required")
    if cfg.get("auto_async", True) is not False and os.environ.get("ESPAUT_STOP_WORKER") != "1":
        # The IDE hook must not wait for acceptance tests, CI, or review polling.
        # A detached worker owns the per-task lock and the full lifecycle.
        try:
            from espaut.stop_worker import launch_worker
            if launch_worker(store, task_id, cwd, preserve_changes=preserve_changes):
                return checkpoint(store, task_id, "running", reason="post-reply lifecycle started")
        except (OSError, ValueError, RuntimeError) as exc:
            return checkpoint(store, task_id, "operational_failure",
                              reason=f"worker launch: {type(exc).__name__}")
    try:
        changes = worktree_status(cwd)
        if changes:
            if not preserve_changes:
                return checkpoint(store, task_id, "blocked", reason="no verified pre-task snapshot")
            result = run_preservation(store, task_id, f"espaut: post-reply {task_id}",
                                      cwd=cwd, dry_run=False,
                                      remote=cfg.get("push_remote", "origin"))
            if result.get("outcome") != "synchronized":
                return checkpoint(store, task_id, "preservation_pending",
                                  reason=result.get("outcome", "unverified"))
        sha = head_sha(cwd)
        if not sha:
            return checkpoint(store, task_id, "blocked", reason="HEAD unavailable")
        push_remote = cfg.get("push_remote", "origin")
        if remote_head_sha(push_remote, branch, cwd) != sha:
            synced = push_and_verify(store, task_id, remote=push_remote,
                                     branch=branch, cwd=cwd)
            if synced.get("status") != "synchronized":
                return checkpoint(store, task_id, "preservation_pending",
                                  revision=sha, reason="existing local commit not verified on remote")
        pr_number = task.get("pr_number")
        if not pr_number:
            if cfg.get("auto_pr") is not True:
                return checkpoint(store, task_id, "pr_pending_authorization",
                                  revision=sha, reason="auto_pr must be true")
            pr = create_or_reuse_pr(
                store, task, task.get("title") or task_id,
                f"Task: {task_id}\n\n{task.get('objective', '')}",
                base=cfg.get("pr_base_branch") or "main", cwd=cwd,
                head_owner=cfg.get("pr_head_owner"))
            pr_number = pr.get("pr_number")
            if pr.get("status") not in ("created", "reused") or not pr_number:
                return checkpoint(store, task_id, "pr_pending",
                                  revision=sha, reason=pr.get("error", "PR not confirmed"))
            update_task_pr(task, int(pr_number), pr.get("url"), head_sha=sha)
            write_json(store / "tasks" / f"{task_id}.json", task)
        pr_number = int(pr_number)
        remote = query_pr_state(pr_number, cwd=cwd)
        if remote.get("status") != "available":
            return checkpoint(store, task_id, "pr_pending", pr_number=pr_number,
                              reason="PR query unavailable")
        if remote.get("merged_at"):
            if not remote.get("merge_commit"):
                return checkpoint(store, task_id, "merge_unverified", pr_number=pr_number,
                                  reason="merged_at present, but merge commit is missing")
            return checkpoint(store, task_id, "merged", pr_number=pr_number,
                              merge_commit=remote["merge_commit"])
        if remote.get("github_state") != "OPEN" or remote.get("head_sha") != sha:
            return checkpoint(store, task_id, "blocked", pr_number=pr_number,
                              revision=sha, reason="PR closed or remote head mismatch")
        if remote.get("is_draft"):
            if cfg.get("auto_ready") is not True:
                return checkpoint(store, task_id, "review_pending", pr_number=pr_number,
                                  revision=sha, reason="PR is Draft; auto_ready is disabled")
            ready = run_gh("pr", "ready", str(pr_number), cwd=cwd)
            if ready.returncode != 0:
                return checkpoint(store, task_id, "review_pending", pr_number=pr_number,
                                  revision=sha, reason=f"GitHub rejected ready-for-review: exit={ready.returncode}")
            remote = query_pr_state(pr_number, cwd=cwd)
            if (remote.get("status") != "available" or remote.get("is_draft")
                    or remote.get("head_sha") != sha or remote.get("github_state") != "OPEN"):
                return checkpoint(store, task_id, "review_pending", pr_number=pr_number,
                                  revision=sha, reason="ready-for-review could not be verified")
        acceptance = verify_acceptance(store, task, sha, cwd=cwd)
        if acceptance.get("status") != "passed":
            return checkpoint(store, task_id, "acceptance_pending", pr_number=pr_number,
                              revision=sha, reason=acceptance.get("reason", "acceptance not verified"))
        checks = query_checks(store, task_id, pr_number, evaluated_revision=sha, cwd=cwd)
        reviews = collect_reviews(store, task_id, pr_number, cwd=cwd)
        reviews.update(is_draft=bool(remote.get("is_draft")),
                       review_decision=remote.get("review_decision"))
        pending = extract_pendencies(reviews, task_id=task_id, store=store)
        decisions = [read_json(p) for p in sorted((store / "decisions").glob("*.json"))]
        gate = evaluate_merge_eligibility(store, task, checks, reviews, pending,
                                           decisions, cwd=cwd)
        gates = {c["criterion"]: c["status"] for c in gate["criteria"]}
        required_review = cfg.get("review_required", True) is not False
        if gate["verdict"] != "APTA_PARA_INTEGRACAO" or (required_review and remote.get("review_decision") != "APPROVED"):
            return checkpoint(store, task_id, "review_pending", pr_number=pr_number,
                              revision=sha, checks=checks.get("aggregate"),
                              pendencies=len(pending), gates=gates,
                              reason="review/CI/acceptance/merge gate pending")
        policy_approved = cfg.get("auto_merge") is True and cfg.get("merge_policy") == "automatic"
        revision_approved = cfg.get("auto_merge") is True and human_approved(task, decisions, sha)
        if not (policy_approved or revision_approved):
            return checkpoint(store, task_id, "merge_pending_authorization",
                              pr_number=pr_number, revision=sha, gates=gates,
                              reason="auto_merge requires a preauthorized project policy or an explicit revision decision")
        # GitHub HEAD must remain exactly the reviewed revision.
        current = pr_view_json(pr_number, ["state", "isDraft", "headRefOid", "mergeStateStatus"], cwd=cwd)
        if (not current or current.get("state") != "OPEN"
                or current.get("isDraft") is not False
                or current.get("headRefOid") != sha
                or current.get("mergeStateStatus") != "CLEAN"):
            return checkpoint(store, task_id, "merge_pending", pr_number=pr_number,
                              revision=sha, reason="PR draft/head/mergeability changed")
        method = cfg.get("merge_method", "merge")
        if method not in ("merge", "squash", "rebase"):
            return checkpoint(store, task_id, "blocked", reason="unsupported merge method")
        response = run_gh("pr", "merge", str(pr_number), f"--{method}",
                          "--match-head-commit", sha, cwd=cwd)
        if response.returncode != 0:
            return checkpoint(store, task_id, "merge_pending", pr_number=pr_number,
                              revision=sha, reason=f"GitHub rejected merge: exit={response.returncode}")
        verified = query_pr_state(pr_number, cwd=cwd)
        if not verified.get("merged_at") or not verified.get("merge_commit"):
            return checkpoint(store, task_id, "merge_unverified", pr_number=pr_number,
                              revision=sha, reason="GitHub did not confirm merge")
        return checkpoint(store, task_id, "merged", pr_number=pr_number,
                          revision=sha, merge_commit=verified["merge_commit"])
    except Exception as exc:
        return checkpoint(store, task_id, "operational_failure",
                          reason=f"{type(exc).__name__}: {str(exc)[:160]}")
