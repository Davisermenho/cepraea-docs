#!/usr/bin/env python3
"""Bounded background continuation for ESPAUT after a VS Code Stop event.

A worker retries pending GitHub checks and review state. It never assumes PASS
from an error or timeout, never bypasses branch protections, and never modifies
files that the coding agent is editing.
"""
from __future__ import annotations

import argparse
import fcntl
import os
import subprocess
import sys
import time
from pathlib import Path

from espaut.store import load_config, read_json
from espaut.stop_cycle import checkpoint, run_stop_cycle


def launch_worker(store: Path, task_id: str, cwd: str, preserve_changes: bool = False) -> bool:
    """Detach one follow-up process; the worker owns the per-task lock."""
    if os.environ.get("ESPAUT_STOP_WORKER") == "1":
        return False
    cfg = load_config(store)
    if cfg.get("auto_commit") is not True or cfg.get("auto_followup", True) is False:
        return False
    cache = store / "cache"
    cache.mkdir(exist_ok=True, parents=True)
    env = os.environ.copy()
    env["ESPAUT_STOP_WORKER"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    package_root = str(Path(__file__).resolve().parents[1])
    env["PYTHONPATH"] = package_root + os.pathsep + env.get("PYTHONPATH", "")
    command = [sys.executable, "-B", "-m", "espaut.stop_worker",
               "--store", str(store), "--task", task_id, "--cwd", cwd]
    if preserve_changes:
        command.append("--preserve-changes")
    with (cache / f"stop-worker-{task_id}.log").open("a", encoding="utf-8") as output:
        subprocess.Popen(command, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                         stdout=output, stderr=subprocess.STDOUT,
                         start_new_session=True, close_fds=True)
    return True


def run_worker(store: Path, task_id: str, cwd: str, preserve_changes: bool = False) -> str:
    """Poll until merge, nonrecoverable block, or an explicit time budget."""
    cfg = load_config(store)
    seconds = cfg.get("followup_interval_seconds", 30)
    budget = cfg.get("followup_timeout_seconds", 3600)
    if type(seconds) is not int or not 5 <= seconds <= 300:
        raise ValueError("followup_interval_seconds must be 5..300")
    if type(budget) is not int or not 60 <= budget <= 86400:
        raise ValueError("followup_timeout_seconds must be 60..86400")
    cache = store / "cache"
    cache.mkdir(exist_ok=True, parents=True)
    with (cache / f"stop-worker-{task_id}.lock").open("a+") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return "already_running"
        deadline = time.monotonic() + budget
        while time.monotonic() < deadline:
            task_file = store / "tasks" / f"{task_id}.json"
            if not task_file.is_file():
                return "missing_task"
            task = read_json(task_file)
            result = run_stop_cycle(store, task, cwd=cwd, preserve_changes=preserve_changes)
            preserve_changes = False
            status = result.get("status", "unknown")
            if status in {"merged", "blocked",
                          "merge_unverified", "preservation_pending",
                          "monitor_only", "pr_pending_authorization",
                          "merge_pending_authorization", "merge_rejected",
                          "merge_rejected_unchanged", "merge_timeout"}:
                return status
            if status not in {"review_pending", "merge_pending", "pr_pending",
                              "operational_failure"}:
                return status
            time.sleep(seconds)
        checkpoint(store, task_id, "followup_timeout",
                   reason="bounded review/check monitoring expired; no merge assumed")
        return "followup_timeout"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--cwd", required=True)
    parser.add_argument("--preserve-changes", action="store_true")
    args = parser.parse_args()
    try:
        status = run_worker(args.store, args.task, args.cwd,
                            preserve_changes=args.preserve_changes)
    except Exception as exc:
        checkpoint(args.store, args.task, "operational_failure",
                   reason=f"worker {type(exc).__name__}: {str(exc)[:160]}")
        status = "operational_failure"
    print(f"ESPAUT followup: {status}", flush=True)
    return 0 if status in {"merged", "already_running"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
