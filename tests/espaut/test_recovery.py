#!/usr/bin/env python3
"""Tests for recovery and traceability."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.events import log_event
from espaut.recovery import (
    audit_task,
    check_idempotency,
    find_last_checkpoint,
    reconstruct_timeline,
    recover_task_state,
)
from espaut.store import init_store, write_json


def _init_repo(path: Path) -> None:
    subprocess.run(["git", "init", str(path)], capture_output=True, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.com"], capture_output=True, check=True, cwd=str(path))
    subprocess.run(["git", "config", "user.name", "T"], capture_output=True, check=True, cwd=str(path))


def _commit(path: Path, fname: str, content: str, msg: str) -> str:
    (path / fname).write_text(content)
    subprocess.run(["git", "add", fname], capture_output=True, check=True, cwd=str(path))
    subprocess.run(["git", "commit", "-m", msg], capture_output=True, check=True, cwd=str(path))
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=str(path),
    ).stdout.strip()


def test_recover_clean() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        sha = _commit(path, "a.txt", "hello", "init")
        store = init_store(path)
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=str(path),
        ).stdout.strip()
        task = {"task_id": "T1", "branch_name": branch, "commit_shas": [sha]}
        result = recover_task_state(store, task, str(path))
        return {"recovered": "PASS" if result["status"] == "recovered" else "FAIL"}


def test_recover_dirty() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        sha = _commit(path, "a.txt", "hello", "init")
        store = init_store(path)
        (path / "a.txt").write_text("changed")
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=str(path),
        ).stdout.strip()
        task = {"task_id": "T1", "branch_name": branch, "commit_shas": [sha]}
        result = recover_task_state(store, task, str(path))
        return {
            "discrepancies": "PASS" if result["status"] == "discrepancies_found" else "FAIL",
            "has_actions": "PASS" if len(result["actions"]) > 0 else "FAIL",
        }


def test_reconstruct_timeline() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "task_created", task_id="T1")
        log_event(store, "commit_created", task_id="T1", object_reference="abc123")
        log_event(store, "task_created", task_id="T2")

        timeline = reconstruct_timeline(store, "T1")
        return {
            "count": "PASS" if len(timeline) == 2 else "FAIL",
            "filtered": "PASS" if all(e["task_id"] == "T1" for e in timeline) else "FAIL",
        }


def test_find_last_checkpoint() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "task_created", task_id="T1")
        log_event(store, "commit_created", task_id="T1", object_reference="sha1")
        log_event(store, "push_verified", task_id="T1", evidence_id="EVD-001")

        cp = find_last_checkpoint(store, "T1")
        return {
            "found": "PASS" if cp is not None else "FAIL",
            "is_push": "PASS" if cp and cp["event_type"] == "push_verified" else "FAIL",
        }


def test_find_no_checkpoint() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "status_check", task_id="T1")
        cp = find_last_checkpoint(store, "T1")
        return {"none": "PASS" if cp is None else "FAIL"}


def test_audit_task() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "task_created", task_id="T1")
        log_event(store, "commit_created", task_id="T1")
        task = {"task_id": "T1", "state": "EM_EXECUCAO", "commit_shas": ["abc"], "pr_number": 42}
        report = audit_task(store, task)
        return {
            "has_events": "PASS" if report["event_count"] == 2 else "FAIL",
            "has_state": "PASS" if report["state"] == "EM_EXECUCAO" else "FAIL",
            "has_commits": "PASS" if report["commits"] == ["abc"] else "FAIL",
        }


def test_idempotency_new() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        done, _ = check_idempotency(store, "T1", "push", "abc123")
        return {"not_done": "PASS" if not done else "FAIL"}


def test_idempotency_duplicate() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "push", task_id="T1", object_reference="abc123", outcome="synchronized")
        done, _ = check_idempotency(store, "T1", "push", "abc123")
        return {"already_done": "PASS" if done else "FAIL"}


ALL_TESTS = [
    ("recover_clean", test_recover_clean),
    ("recover_dirty", test_recover_dirty),
    ("reconstruct_timeline", test_reconstruct_timeline),
    ("find_last_checkpoint", test_find_last_checkpoint),
    ("find_no_checkpoint", test_find_no_checkpoint),
    ("audit_task", test_audit_task),
    ("idempotency_new", test_idempotency_new),
    ("idempotency_duplicate", test_idempotency_duplicate),
]


def main() -> int:
    total_pass = 0
    total_checks = 0

    for name, fn in ALL_TESTS:
        try:
            checks = fn()
        except Exception as exc:
            print(f"  [FAIL] {name} — exception: {exc}")
            total_checks += 1
            continue

        for sub, status in checks.items():
            total_checks += 1
            if status == "PASS":
                total_pass += 1
            print(f"  [{status}] {name}.{sub}")

    print(f"\nrecovery: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
