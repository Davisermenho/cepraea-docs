#!/usr/bin/env python3
"""C1 must respect explicit eligible_patterns without weakening revision/authority gates."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from espaut.governance import check_c1_preservation, evaluate_merge_eligibility
from espaut.store import init_store, write_json


EXCLUDED = [
    {"index": " ", "worktree": "M",
     "path": "espaut/__pycache__/cli.cpython-312.pyc"},
    {"index": "?", "worktree": "?", "path": "unrelated.txt"},
]
ELIGIBLE = {"index": " ", "worktree": "M", "path": "espaut-hook-pr-check.txt"}


class PreservationScopeTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.store = init_store(self.root)
        write_json(self.store / "config.json", {
            "eligible_patterns": ["espaut-hook-pr-check.txt"],
            "review_required": False,
            "auto_merge": False,
            "ci_required": False,
        })

    def test_only_excluded_paths_are_explicitly_dispensed(self):
        with patch("espaut.git_ops.worktree_status", return_value=EXCLUDED):
            result = check_c1_preservation({}, str(self.root),
                                           eligible_patterns=["espaut-hook-pr-check.txt"])
        self.assertEqual(result["status"], "PASS")
        self.assertIn("excluded by project policy", result["detail"])

    def test_eligible_uncommitted_path_blocks(self):
        with patch("espaut.git_ops.worktree_status", return_value=EXCLUDED + [ELIGIBLE]):
            result = check_c1_preservation({}, str(self.root),
                                           eligible_patterns=["espaut-hook-pr-check.txt"])
        self.assertEqual(result["status"], "FAIL")

    def test_unspecified_patterns_keep_original_strictness(self):
        with patch("espaut.git_ops.worktree_status", return_value=EXCLUDED):
            result = check_c1_preservation({}, str(self.root))
        self.assertEqual(result["status"], "FAIL")

    def test_c1_scope_passes_but_c7_stays_blocked(self):
        sha = "a" * 40
        task = {
            "task_id": "T-C1",
            "acceptance_criteria": ["PR_FILE_V2"],
            "acceptance_revision": sha,
            "acceptance_results": {
                "PR_FILE_V2": {
                    "status": "PASS",
                    "revision": sha,
                    "evidence_reference": "acceptance-test.json",
                }
            },
        }
        checks = {
            "status": "not_configured",
            "aggregate": "NAO_CONFIGURADO",
            "evaluated_revision": sha,
            "checks": [],
        }
        with patch("espaut.governance.head_sha", return_value=sha), \
             patch("espaut.git_ops.worktree_status", return_value=EXCLUDED), \
             patch("espaut.governance.check_c2_sync",
                   return_value={"criterion": "C2_sync", "status": "PASS", "detail": "synced"}):
            result = evaluate_merge_eligibility(
                self.store, task, checks, {"reviews": []}, [], [],
                cwd=str(self.root),
            )
        statuses = {x["criterion"]: x["status"] for x in result["criteria"]}
        self.assertEqual(statuses["C1_preservation"], "PASS")
        self.assertEqual(statuses["C6_acceptance"], "PASS")
        self.assertEqual(statuses["C7_authority"], "FAIL")
        self.assertEqual(result["verdict"], "NAO_APTA")


if __name__ == "__main__":
    unittest.main(verbosity=2)
