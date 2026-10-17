#!/usr/bin/env python3
"""GitHub CLI (gh) wrappers using parameterized subprocess calls."""

from __future__ import annotations

import json
import subprocess
from typing import Any

from espaut.security import validate_subprocess_args


def run_gh(
    *args: str,
    timeout: int = 60,
    cwd: str | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a gh CLI command with validated arguments."""
    cmd = ["gh", *args]
    validate_subprocess_args(cmd)
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        cwd=cwd,
    )


def gh_available() -> bool:
    """Return True if the gh CLI is installed and authenticated."""
    r = run_gh("auth", "status", timeout=10)
    return r.returncode == 0


def pr_list_json(
    fields: list[str] | None = None,
    state: str = "open",
    cwd: str | None = None,
) -> list[dict[str, Any]]:
    """List PRs as parsed JSON."""
    field_list = fields or ["number", "title", "headRefName", "state", "url"]
    r = run_gh(
        "pr", "list",
        "--state", state,
        "--json", ",".join(field_list),
        cwd=cwd,
    )
    if r.returncode != 0:
        return []
    return json.loads(r.stdout)


def pr_view_json(
    pr_ref: str | int,
    fields: list[str] | None = None,
    cwd: str | None = None,
) -> dict[str, Any] | None:
    """Query a PR's fields as JSON."""
    field_list = fields or [
        "number", "title", "headRefName", "baseRefName",
        "state", "url", "headRefOid", "mergeCommit", "mergedAt",
    ]
    r = run_gh(
        "pr", "view", str(pr_ref),
        "--json", ",".join(field_list),
        cwd=cwd,
    )
    if r.returncode != 0:
        return None
    return json.loads(r.stdout)


def pr_create(
    title: str,
    body: str,
    base: str | None = None,
    head: str | None = None,
    cwd: str | None = None,
) -> dict[str, Any] | None:
    """Create a PR and return its data (via pr view after creation).

    ``gh pr create`` outputs the new PR's URL to stdout; ``--json`` is not
    supported.  After a successful create we call ``pr_view_json`` to
    retrieve the structured representation.
    """
    args = ["pr", "create", "--title", title, "--body", body]
    if base:
        args.extend(["--base", base])
    if head:
        args.extend(["--head", head])
    r = run_gh(*args, cwd=cwd)
    if r.returncode != 0:
        return None
    url = r.stdout.strip()
    view = pr_view_json(url, cwd=cwd) if url else None
    if view:
        return view
    return {"url": url}


def pr_checks_json(
    pr_ref: str | int,
    cwd: str | None = None,
) -> list[dict[str, Any]]:
    """Query check/status results for a PR."""
    r = run_gh(
        "pr", "checks", str(pr_ref),
        "--json", "name,state,bucket,description,startedAt,completedAt,link,workflow",
        cwd=cwd,
    )
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def pr_reviews_json(
    pr_number: int,
    cwd: str | None = None,
) -> list[dict[str, Any]]:
    """Query reviews for a PR via the REST API."""
    r = run_gh(
        "api",
        f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/reviews",
        "--jq", ".",
        cwd=cwd,
    )
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def pr_comments_json(
    pr_number: int,
    cwd: str | None = None,
) -> list[dict[str, Any]]:
    """Query issue-level comments on a PR."""
    r = run_gh(
        "api",
        f"repos/{{owner}}/{{repo}}/issues/{pr_number}/comments",
        "--jq", ".",
        cwd=cwd,
    )
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def pr_review_comments_json(
    pr_number: int,
    cwd: str | None = None,
) -> list[dict[str, Any]]:
    """Query code-level review comments on a PR."""
    r = run_gh(
        "api",
        f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/comments",
        "--jq", ".",
        cwd=cwd,
    )
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def pr_merge(
    pr_ref: str | int,
    method: str = "merge",
    cwd: str | None = None,
) -> subprocess.CompletedProcess[str]:
    """Merge a PR. method: merge, squash, or rebase.

    ``gh pr merge`` does not support ``--json``; success is indicated by
    a zero return code.
    """
    return run_gh(
        "pr", "merge", str(pr_ref),
        f"--{method}",
        "--yes",
        cwd=cwd,
    )
