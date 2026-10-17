#!/usr/bin/env python3
"""Tests for triggers, sync, and conflict detection."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.triggers import (
    check_base_branch_updated,
    check_sync_state,
    detect_pending_preservation,
)
from espaut.store import init_store


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


def test_sync_no_remote() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _commit(path, "a.txt", "init", "init")
        store = init_store(path)
        result = check_sync_state(store, "T1", cwd=str(path))
        return {"no_remote": "PASS" if result["status"] == "no_remote" else "FAIL"}


def test_sync_local_ahead() -> dict[str, str]:
    """Simulate local ahead by mocking remote_head_sha to return an ancestor."""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        sha1 = _commit(path, "a.txt", "init", "init")
        sha2 = _commit(path, "a.txt", "v2", "update")
        store = init_store(path)

        with patch("espaut.triggers.remote_head_sha", return_value=sha1):
            result = check_sync_state(store, "T1", cwd=str(path))
            return {"ahead": "PASS" if result["status"] == "local_ahead" else f"FAIL: {result['status']}"}


def test_base_branch_unchanged() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        sha = "abc123"
        with patch("espaut.triggers.remote_head_sha", return_value=sha):
            result = check_base_branch_updated(store, "T1", "main", sha, cwd=str(tmp))
            return {"unchanged": "PASS" if result["status"] == "unchanged" else "FAIL"}


def test_base_branch_updated() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        with patch("espaut.triggers.remote_head_sha", return_value="new_sha"):
            result = check_base_branch_updated(store, "T1", "main", "old_sha", cwd=str(tmp))
            return {"updated": "PASS" if result["status"] == "updated" else "FAIL"}


def test_detect_clean() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _commit(path, "a.txt", "init", "init")
        store = init_store(path)
        result = detect_pending_preservation(store, "T1", str(path))
        return {"clean": "PASS" if result["status"] == "clean" else "FAIL"}


def test_detect_pending() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _commit(path, "a.txt", "init", "init")
        store = init_store(path)
        (path / "a.txt").write_text("changed")
        result = detect_pending_preservation(store, "T1", str(path))
        return {
            "pending": "PASS" if result["status"] == "pending" else "FAIL",
            "has_eligible": "PASS" if len(result.get("eligible", [])) > 0 else "FAIL",
        }


ALL_TESTS = [
    ("sync_no_remote", test_sync_no_remote),
    ("sync_local_ahead", test_sync_local_ahead),
    ("base_unchanged", test_base_branch_unchanged),
    ("base_updated", test_base_branch_updated),
    ("detect_clean", test_detect_clean),
    ("detect_pending", test_detect_pending),
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

    print(f"\ntriggers: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
