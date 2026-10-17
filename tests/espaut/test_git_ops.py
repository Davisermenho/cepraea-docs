#!/usr/bin/env python3
"""Tests for git_ops.py using real temporary git repositories."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.git_ops import (
    branch_exists,
    create_branch,
    current_branch,
    has_changes,
    has_incomplete_operation,
    head_sha,
    is_git_repo,
    is_ref_valid,
    repo_root,
    staged_diff,
    staged_files,
    worktree_status,
)


def _init_repo(path: Path) -> None:
    subprocess.run(["git", "init", str(path)], capture_output=True, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@test.com"],
        capture_output=True, check=True, cwd=str(path),
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        capture_output=True, check=True, cwd=str(path),
    )


def _make_commit(path: Path, filename: str, content: str, msg: str) -> None:
    (path / filename).write_text(content)
    subprocess.run(["git", "add", filename], capture_output=True, check=True, cwd=str(path))
    subprocess.run(["git", "commit", "-m", msg], capture_output=True, check=True, cwd=str(path))


def test_is_git_repo() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        checks: dict[str, str] = {}
        checks["not_repo"] = "PASS" if not is_git_repo(str(path)) else "FAIL"
        _init_repo(path)
        checks["is_repo"] = "PASS" if is_git_repo(str(path)) else "FAIL"
        return checks


def test_repo_root() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        root = repo_root(str(path))
        sub = path / "sub" / "deep"
        sub.mkdir(parents=True)
        root_from_sub = repo_root(str(sub))
        return {
            "root_found": "PASS" if root is not None else "FAIL",
            "root_from_subdir": "PASS" if root_from_sub == root else "FAIL",
        }


def test_current_branch_and_head() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "hello", "initial commit")

        branch = current_branch(str(path))
        sha = head_sha(str(path))
        return {
            "has_branch": "PASS" if branch is not None else "FAIL",
            "has_sha": "PASS" if sha and len(sha) == 40 else "FAIL",
        }


def test_worktree_status() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "tracked.txt", "initial", "init")

        checks: dict[str, str] = {}
        entries = worktree_status(str(path))
        checks["clean"] = "PASS" if len(entries) == 0 else "FAIL"

        (path / "tracked.txt").write_text("modified")
        entries = worktree_status(str(path))
        checks["modified"] = "PASS" if len(entries) == 1 and entries[0]["worktree"] == "M" else "FAIL"

        (path / "new.txt").write_text("untracked")
        entries = worktree_status(str(path))
        checks["untracked"] = "PASS" if any(e["index"] == "?" for e in entries) else "FAIL"

        return checks


def test_has_changes() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "hello", "init")

        checks: dict[str, str] = {}
        checks["clean"] = "PASS" if not has_changes(str(path)) else "FAIL"
        (path / "a.txt").write_text("changed")
        checks["dirty"] = "PASS" if has_changes(str(path)) else "FAIL"
        return checks


def test_staging_and_diff() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "line1\n", "init")

        (path / "a.txt").write_text("line1\nline2\n")
        subprocess.run(["git", "add", "a.txt"], capture_output=True, check=True, cwd=str(path))

        files = staged_files(str(path))
        diff = staged_diff(str(path))
        return {
            "staged_files": "PASS" if files == ["a.txt"] else "FAIL",
            "diff_not_empty": "PASS" if "line2" in diff else "FAIL",
        }


def test_branch_operations() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "init", "initial")

        checks: dict[str, str] = {}
        checks["not_exists"] = "PASS" if not branch_exists("feature", str(path)) else "FAIL"
        create_branch("feature", cwd=str(path))
        checks["exists"] = "PASS" if branch_exists("feature", str(path)) else "FAIL"
        return checks


def test_ref_valid() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "init", "initial")

        sha = head_sha(str(path))
        return {
            "head_valid": "PASS" if is_ref_valid("HEAD", str(path)) else "FAIL",
            "sha_valid": "PASS" if sha and is_ref_valid(sha, str(path)) else "FAIL",
            "bogus_invalid": "PASS" if not is_ref_valid("bogus123", str(path)) else "FAIL",
        }


def test_incomplete_operation() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        _init_repo(path)
        _make_commit(path, "a.txt", "init", "initial")
        return {
            "no_incomplete": "PASS" if has_incomplete_operation(str(path)) is None else "FAIL",
        }


ALL_TESTS = [
    ("is_git_repo", test_is_git_repo),
    ("repo_root", test_repo_root),
    ("current_branch_and_head", test_current_branch_and_head),
    ("worktree_status", test_worktree_status),
    ("has_changes", test_has_changes),
    ("staging_and_diff", test_staging_and_diff),
    ("branch_operations", test_branch_operations),
    ("ref_valid", test_ref_valid),
    ("incomplete_operation", test_incomplete_operation),
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

    print(f"\ngit_ops: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
