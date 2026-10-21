#!/usr/bin/env python3
"""Focused regression tests for observable, bounded automatic merge attempts."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from espaut import stop_cycle
from espaut.gh_ops import gh_command_diagnostic
from espaut.store import init_store, read_json


REVISION = "a" * 40
REPOSITORY = "Davisermenho/cepraea-docs"


def completed(code=0, stdout="", stderr=""):
    return subprocess.CompletedProcess(["gh"], code, stdout, stderr)


def remote(*, merged=False):
    return {
        "status": "available",
        "github_state": "MERGED" if merged else "OPEN",
        "merged_at": "2026-10-21T01:00:00Z" if merged else None,
        "merge_commit": {"oid": "b" * 40} if merged else None,
    }


class MergeExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = init_store(self.root)
        self.kwargs = {
            "pr_number": 4,
            "revision": REVISION,
            "method": "merge",
            "repository": REPOSITORY,
            "cwd": str(self.root),
            "conditions": {
                "repository": REPOSITORY,
                "revision": REVISION,
                "review_decision": "APPROVED",
                "merge_state": "CLEAN",
            },
        }

    def execute(self):
        return stop_cycle.execute_merge(
            self.store, "TASK-D08", **self.kwargs
        )

    def test_success_requires_remote_confirmation(self):
        with patch.object(stop_cycle, "run_gh", return_value=completed(0)), \
             patch.object(stop_cycle, "query_pr_state", return_value=remote(merged=True)):
            result = self.execute()
        self.assertEqual(result["status"], "merged")
        self.assertEqual(result["merge_commit"]["oid"], "b" * 40)
        self.assertEqual(result["merge_attempt"]["exit_code"], 0)

    def test_exit_zero_without_remote_confirmation_is_not_success(self):
        with patch.object(stop_cycle, "run_gh", return_value=completed(0)), \
             patch.object(stop_cycle, "query_pr_state", return_value=remote()):
            result = self.execute()
        self.assertEqual(result["status"], "merge_unverified")

    def test_rejection_preserves_sanitized_diagnostic(self):
        secret = "gho_" + "x" * 40
        response = completed(
            1, "request refused", f"GraphQL: resource not accessible; token={secret}"
        )
        with patch.object(stop_cycle, "run_gh", return_value=response), \
             patch.object(stop_cycle, "query_pr_state", return_value=remote()):
            result = self.execute()
        self.assertEqual(result["status"], "merge_rejected")
        attempt = result["merge_attempt"]
        self.assertEqual(attempt["exit_code"], 1)
        self.assertEqual(attempt["failure_class"], "permission_denied")
        self.assertIn("[REDACTED]", attempt["stderr"])
        self.assertNotIn(secret, str(result))
        self.assertEqual(attempt["repository"], REPOSITORY)
        self.assertEqual(attempt["command"][0:3], ["gh", "pr", "merge"])

    def test_equivalent_rejection_is_not_retried(self):
        with patch.object(stop_cycle, "run_gh", return_value=completed(1, stderr="not mergeable")) as execute, \
             patch.object(stop_cycle, "query_pr_state", return_value=remote()):
            first = self.execute()
            second = self.execute()
        self.assertEqual(first["status"], "merge_rejected")
        self.assertEqual(second["status"], "merge_rejected_unchanged")
        self.assertEqual(execute.call_count, 1)

    def test_changed_condition_allows_new_attempt(self):
        with patch.object(stop_cycle, "run_gh", return_value=completed(1, stderr="not mergeable")) as execute, \
             patch.object(stop_cycle, "query_pr_state", return_value=remote()):
            self.execute()
            self.kwargs["conditions"] = {**self.kwargs["conditions"], "merge_state": "NEW_STATE"}
            self.execute()
        self.assertEqual(execute.call_count, 2)

    def test_timeout_is_recorded_and_not_assumed_success(self):
        timeout = subprocess.TimeoutExpired(
            ["gh", "pr", "merge"], 60,
            output="partial output", stderr="request timed out",
        )
        with patch.object(stop_cycle, "run_gh", side_effect=timeout), \
             patch.object(stop_cycle, "query_pr_state", return_value=remote()):
            result = self.execute()
        self.assertEqual(result["status"], "merge_timeout")
        self.assertTrue(result["merge_attempt"]["timed_out"])
        self.assertEqual(result["merge_attempt"]["failure_class"], "timeout")

    def test_timeout_can_still_be_remotely_confirmed(self):
        timeout = subprocess.TimeoutExpired(["gh"], 60, stderr="timeout")
        with patch.object(stop_cycle, "run_gh", side_effect=timeout), \
             patch.object(stop_cycle, "query_pr_state", return_value=remote(merged=True)):
            result = self.execute()
        self.assertEqual(result["status"], "merged")

    def test_worker_treats_rejection_as_terminal(self):
        from espaut import stop_worker
        task = {"task_id": "TASK-D08"}
        task_path = self.store / "tasks" / "TASK-D08.json"
        task_path.write_text(__import__("json").dumps(task), encoding="utf-8")
        with patch.object(stop_worker, "load_config", return_value={
                 "followup_interval_seconds": 5,
                 "followup_timeout_seconds": 60,
             }), patch.object(stop_worker, "run_stop_cycle", return_value={
                 "status": "merge_rejected"
             }) as cycle:
            status = stop_worker.run_worker(
                self.store, "TASK-D08", str(self.root)
            )
        self.assertEqual(status, "merge_rejected")
        self.assertEqual(cycle.call_count, 1)

    def test_direct_diagnostic_redacts_authorization(self):
        diagnostic = gh_command_diagnostic(
            ["api", "user"], repository=REPOSITORY, returncode=1,
            stderr="Authorization: Bearer top-secret-value-123456789",
        )
        self.assertNotIn("top-secret-value", diagnostic["stderr"])
        self.assertIn("[REDACTED]", diagnostic["stderr"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
