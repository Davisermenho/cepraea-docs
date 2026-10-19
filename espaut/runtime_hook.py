#!/usr/bin/env python3
"""Canonical global lifecycle dispatcher for Claude Code and Codex."""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

from espaut import __version__
from espaut.git_ops import current_branch, head_sha, repo_root, worktree_status
from espaut.preservation import classify_changes
from espaut.store import load_config, read_json, write_json
from espaut.task import make_task


def _runtime_root() -> Path:
    # .../<runtime>/versions/<release>/espaut/runtime_hook.py
    resolved = Path(__file__).resolve()
    return resolved.parents[3]


def _manifest() -> dict[str, Any]:
    path = PACKAGE_ROOT / "release-manifest.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"version": __version__, "implementation_sha": "unknown"}


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds")


def _event_log(record: dict[str, Any]) -> None:
    state = _runtime_root() / "state"
    state.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = state / "events.jsonl"
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _git_root(cwd: str) -> Path | None:
    root = repo_root(cwd)
    return Path(root).resolve() if root else None


def _project_has_legacy_hook(root: Path, provider: str) -> bool:
    path = root / (".codex/hooks.json" if provider == "codex" else ".claude/settings.json")
    if not path.is_file():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    return "espaut/ide_hook.py" in text or "espaut\\ide_hook.py" in text


def _task_for(store: Path, branch: str) -> dict[str, Any] | None:
    tasks = []
    for path in sorted((store / "tasks").glob("TASK-*.json")):
        try:
            task = read_json(path)
        except (OSError, ValueError):
            continue
        if task.get("branch_name") == branch and task.get("state") not in {
            "INTEGRADA", "ENCERRADA_SEM_MERGE", "INTERROMPIDA",
        }:
            tasks.append(task)
    return tasks[0] if len(tasks) == 1 else None


def _task_for_or_create(
    store: Path, root: Path, branch: str, config: dict[str, Any], session: str,
) -> tuple[dict[str, Any] | None, bool]:
    task = _task_for(store, branch)
    if task is not None:
        return task, False
    active = []
    for path in sorted((store / "tasks").glob("TASK-*.json")):
        try:
            candidate = read_json(path)
        except (OSError, ValueError):
            continue
        if (candidate.get("branch_name") == branch
                and candidate.get("state") not in {"INTEGRADA", "ENCERRADA_SEM_MERGE", "INTERROMPIDA"}):
            active.append(candidate)
    if active or config.get("auto_task") is not True:
        return None, False
    task_id = "TASK-" + hashlib.sha256(f"{root}|{branch}".encode()).hexdigest()[:12]
    task = make_task(
        task_id=task_id,
        repository_id=config.get("github_repository") or str(root),
        title=f"ESPAUT: {branch}",
        objective="Tarefa associada automaticamente ao ciclo da IDE.",
        authorized_scope=list(config.get("eligible_patterns") or []),
        acceptance_criteria=list(config.get("default_acceptance_criteria") or []),
    )
    task["branch_name"] = branch
    task["base_commit_sha"] = head_sha(str(root))
    task["head_commit_sha"] = head_sha(str(root))
    task["sessions"] = [session]
    write_json(store / "tasks" / f"{task_id}.json", task)
    return task, True


def _dedupe_key(provider: str, phase: str, payload: dict[str, Any], root: Path, paths: list[str]) -> str:
    prompt = payload.get("prompt") if isinstance(payload.get("prompt"), str) else ""
    identity = {
        "provider": provider,
        "phase": phase,
        "root": str(root),
        "session": payload.get("session_id"),
        "turn": payload.get("turn_id"),
        "event": payload.get("hook_event_name"),
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest() if prompt else None,
        "paths": paths,
    }
    return hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()


def _claim_event(key: str, ttl: int = 5) -> bool:
    claims = _runtime_root() / "state" / "claims"
    claims.mkdir(parents=True, exist_ok=True, mode=0o700)
    claim = claims / f"{key}.json"
    now = time.time()
    try:
        existing = json.loads(claim.read_text(encoding="utf-8"))
        if now - float(existing.get("time", 0)) < ttl:
            return False
    except (OSError, ValueError, TypeError):
        pass
    temp = claim.with_suffix(".tmp")
    temp.write_text(json.dumps({"time": now}), encoding="utf-8")
    os.replace(temp, claim)
    return True


def dispatch(provider: str, phase: str, payload: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    manifest = _manifest()
    cwd = payload.get("cwd")
    session = payload.get("session_id")
    base = {
        "occurred_at": _now(),
        "provider": provider,
        "phase": phase,
        "triggering_hook": payload.get("hook_event_name") or phase,
        "session_id": session if isinstance(session, str) else None,
        "turn_id": payload.get("turn_id"),
        "runtime_version": manifest.get("version", __version__),
        "implementation_sha": manifest.get("implementation_sha", "unknown"),
    }
    if not isinstance(cwd, str) or not Path(cwd).is_dir():
        return "ESPAUT: diretório do projeto inválido; nenhuma ação executada.", {**base, "outcome": "invalid_cwd"}
    root = _git_root(cwd)
    if root is None:
        return "", {**base, "worktree": cwd, "outcome": "not_git"}
    base["worktree"] = str(root)
    store = root / ".espaut"
    if _project_has_legacy_hook(root, provider):
        return "", {**base, "outcome": "delegated_to_project_hook"}
    if not (store / "config.json").is_file():
        return "ESPAUT: proteção ativa em modo monitor; projeto ainda não autorizado.", {**base, "outcome": "monitor_only"}
    try:
        entries = worktree_status(str(root))
    except RuntimeError:
        return "ESPAUT: não foi possível verificar o Git; ações automáticas bloqueadas.", {**base, "outcome": "git_unavailable"}
    paths = sorted({entry["path"] for entry in entries})
    key = _dedupe_key(provider, phase, payload, root, paths)
    base["event_id"] = key
    if not _claim_event(key):
        return "", {**base, "outcome": "duplicate_suppressed"}
    if not isinstance(session, str) or not session.strip():
        return "ESPAUT: sessão sem identidade confiável; ações automáticas bloqueadas.", {**base, "outcome": "session_missing"}
    cfg = load_config(store)
    base["policy_version"] = cfg.get("policy_version") or cfg.get("schema_version")
    branch = current_branch(str(root))
    associated_task = None
    task_created = False
    if branch and branch not in {"main", "master"}:
        associated_task, task_created = _task_for_or_create(
            store, root, branch, cfg, session,
        )
        if associated_task:
            base["task_id"] = associated_task["task_id"]
    session_key = hashlib.sha256(f"{provider}|{root}|{session}".encode()).hexdigest()
    snapshot = _runtime_root() / "state" / "snapshots" / f"{session_key}.json"
    snapshot.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if phase == "pre":
        snapshot.write_text(json.dumps({
            "provider": provider, "root": str(root), "session_id": session,
            "dirty": paths, "input_sha": head_sha(str(root)), "created_at": _now(),
        }, sort_keys=True), encoding="utf-8")
        return "", {
            **base,
            "outcome": "task_created_snapshot" if task_created else "snapshot",
            "input_sha": head_sha(str(root)), "changed_count": len(paths),
        }
    if phase != "post":
        return "", {**base, "outcome": "ignored_phase"}

    patterns = cfg.get("eligible_patterns")
    if cfg.get("auto_commit") is not True or not isinstance(patterns, list) or not patterns:
        return "ESPAUT: política do projeto não autoriza preservação automática.", {**base, "outcome": "opt_in_missing"}
    if not all(isinstance(pattern, str) and pattern for pattern in patterns):
        return "ESPAUT: eligible_patterns inválido; ações bloqueadas.", {**base, "outcome": "invalid_policy"}
    previous: dict[str, Any] = {}
    if snapshot.is_file():
        try:
            previous = json.loads(snapshot.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return "ESPAUT: snapshot anterior inválido; ações bloqueadas.", {**base, "outcome": "snapshot_invalid"}
    before = set(previous.get("dirty", []))
    eligible_now, _ = classify_changes(entries, patterns)
    preexisting_eligible = sorted(path for path in before if any(fnmatch.fnmatch(path, pattern) for pattern in patterns))
    newly_eligible = sorted(set(eligible_now) - before)
    if newly_eligible and (not previous or previous.get("root") != str(root)):
        return "ESPAUT: snapshot pré-tarefa ausente; commit automático bloqueado.", {**base, "outcome": "snapshot_missing"}
    if preexisting_eligible:
        return "ESPAUT: alteração elegível preexistente preservada sem commit automático.", {**base, "outcome": "preexisting_eligible", "eligible": preexisting_eligible}
    if not branch or branch in {"main", "master"}:
        return "ESPAUT: branch protegida; nenhuma alteração Git executada.", {**base, "outcome": "protected_branch"}
    task = associated_task or _task_for(store, branch)
    if task is None:
        return "ESPAUT: é necessária uma única tarefa ativa vinculada à branch.", {**base, "outcome": "task_ambiguous"}
    from espaut.stop_worker import launch_worker
    launched = launch_worker(store, task["task_id"], str(root), preserve_changes=bool(newly_eligible))
    if not launched:
        return "ESPAUT: worker não iniciado; política ou concorrência impediu a execução.", {**base, "outcome": "worker_not_started", "task_id": task["task_id"]}
    return "ESPAUT: ciclo Git/GitHub enfileirado.", {
        **base, "outcome": "queued", "task_id": task["task_id"],
        "input_sha": previous.get("input_sha"), "output_sha": head_sha(str(root)),
        "new_eligible": newly_eligible,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=("codex", "claude"), required=True)
    parser.add_argument("--phase", choices=("pre", "post"), required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = json.loads(sys.stdin.buffer.read(262144))
        if not isinstance(payload, dict):
            payload = {}
    except (OSError, ValueError):
        payload = {}
    lock_path = _runtime_root() / "state" / "dispatcher.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with lock_path.open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            message, record = dispatch(args.provider, args.phase, payload)
        except Exception as exc:
            message = f"ESPAUT: falha segura ({type(exc).__name__}); nenhum sucesso presumido."
            record = {
                "occurred_at": _now(), "provider": args.provider, "phase": args.phase,
                "runtime_version": __version__, "outcome": "error", "cause": type(exc).__name__,
            }
        _event_log(record)
    if args.phase == "post":
        response: dict[str, Any] = {"continue": True}
        if message:
            response["systemMessage"] = message
        print(json.dumps(response, ensure_ascii=False))
    elif message:
        print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
