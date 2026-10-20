#!/usr/bin/env python3
"""Regression: excluded dirty artifacts must not block post-Stop PR reconciliation."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from espaut import stop_cycle
from espaut.store import init_store, write_json


class ExcludedArtifactsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = init_store(self.root)
        self.task = {
            "task_id": "TASK-EXCLUDED",
            "branch_name": "test/espaut-stop",
            "pr_number": 2,
            "acceptance_criteria": ["PR_FILE_V2"],
        }
        write_json(self.store / "config.json", {
            "auto_commit": True,
            "eligible_patterns": ["espaut-hook-pr-check.txt"],
            "push_remote": "fork",
            "auto_pr": True,
            "auto_merge": False,
            "auto_async": False,
        })
        self.sha = "f" * 40
        self.clean_remote = {
            "status": "available",
            "github_state": "OPEN",
            "head_sha": self.sha,
            "base_branch": "main",
            "is_draft": False,
            "review_decision": None,
        }

    def _run(self, status_entries, preserve_changes):
        with patch.object(stop_cycle, "current_branch", return_value="test/espaut-stop"), \
             patch.object(stop_cycle, "has_incomplete_operation", return_value=None), \
             patch.object(stop_cycle, "worktree_status", return_value=status_entries), \
             patch.object(stop_cycle, "head_sha", return_value=self.sha), \
             patch.object(stop_cycle, "remote_head_sha", return_value=self.sha), \
             patch.object(stop_cycle, "repository_slug", return_value="Davisermenho/cepraea-docs"), \
             patch.object(stop_cycle, "repository_info", return_value={"nameWithOwner": "Davisermenho/cepraea-docs", "viewerPermission": "READ"}), \
             patch.object(stop_cycle, "query_pr_state", return_value=self.clean_remote), \
             patch.object(stop_cycle, "verify_acceptance", return_value={"status": "passed"}) as acceptance, \
             patch.object(stop_cycle, "run_preservation") as preservation, \
             patch.object(stop_cycle, "query_checks", return_value={"aggregate": "APROVADO"}), \
             patch.object(stop_cycle, "collect_reviews", return_value={"reviews": []}), \
             patch.object(stop_cycle, "extract_pendencies", return_value=[]), \
             patch.object(stop_cycle, "evaluate_merge_eligibility",
                          return_value={"verdict": "NAO_APTA", "criteria": []}):
            preservation.return_value = {"outcome": "synchronized"}
            result = stop_cycle.run_stop_cycle(
                self.store, self.task, cwd=str(self.root),
                preserve_changes=preserve_changes)
            return result, acceptance.call_count, preservation.call_count

    def test_excluded_pycs_allow_acceptance_with_no_new_snapshot(self):
        dirty = [
            {"index": " ", "worktree": "M", "path": "espaut/__pycache__/cli.cpython-312.pyc"},
            {"index": "?", "worktree": "?", "path": "old-untracked.txt"},
        ]
        result, acceptance_calls, preservation_calls = self._run(
            dirty, preserve_changes=False)
        self.assertEqual(result["status"], "review_pending")
        self.assertEqual(acceptance_calls, 1)
        self.assertEqual(preservation_calls, 0)

    def test_preexisting_eligible_file_still_blocks(self):
        dirty = [
            {"index": "?", "worktree": "?", "path": "espaut-hook-pr-check.txt"},
            {"index": " ", "worktree": "M", "path": "espaut/__pycache__/cli.cpython-312.pyc"},
        ]
        result, acceptance_calls, preservation_calls = self._run(
            dirty, preserve_changes=False)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(acceptance_calls, 0)
        self.assertEqual(preservation_calls, 0)
        self.assertEqual(result["eligible"], ["espaut-hook-pr-check.txt"])

    def test_new_eligible_file_preserved_when_snapshot_is_verified(self):
        dirty = [{"index": "?", "worktree": "?",
                  "path": "espaut-hook-pr-check.txt"}]
        result, acceptance_calls, preservation_calls = self._run(
            dirty, preserve_changes=True)
        self.assertEqual(result["status"], "review_pending")
        self.assertEqual(acceptance_calls, 1)
        self.assertEqual(preservation_calls, 1)

    def test_no_dirty_files_allows_acceptance(self):
        result, acceptance_calls, preservation_calls = self._run(
            [], preserve_changes=False)
        self.assertEqual(result["status"], "review_pending")
        self.assertEqual(acceptance_calls, 1)
        self.assertEqual(preservation_calls, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
