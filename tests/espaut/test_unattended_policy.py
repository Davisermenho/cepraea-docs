#!/usr/bin/env python3
"""Regression tests for the explicitly preapproved, unattended GitHub policy."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from espaut.governance import check_c4_review, check_c7_authority
from espaut.acceptance import verify_acceptance
from espaut.store import init_store, write_json, read_json


class UnattendedPolicyTests(unittest.TestCase):
    def test_default_policy_still_requires_authorization(self):
        task = {"task_id": "T1"}
        self.assertEqual(check_c7_authority(task, [])["status"], "FAIL")

    def test_preapproved_policy_does_not_require_per_sha_approval(self):
        task = {"task_id": "T1"}
        self.assertEqual(check_c7_authority(task, [], automatic_policy=True)["status"], "PASS")

    def test_optional_review_does_not_bypass_changes_requested(self):
        report = {"reviews": [], "review_decision": "CHANGES_REQUESTED", "is_draft": False}
        self.assertEqual(check_c4_review(report, review_required=False)["status"], "FAIL")

    def test_optional_review_blocks_draft(self):
        report = {"reviews": [], "review_decision": None, "is_draft": True}
        self.assertEqual(check_c4_review(report, review_required=False)["status"], "FAIL")

    def test_optional_review_allows_approved_policy_when_no_objections(self):
        report = {"reviews": [], "review_decision": None, "is_draft": False}
        self.assertEqual(check_c4_review(report, review_required=False)["status"], "PASS")

    def test_acceptance_requires_per_criterion_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            store = init_store(base)
            task = {"task_id": "TASK-T", "acceptance_criteria": ["a", "b"]}
            write_json(store / "config.json",
                       {"acceptance_commands": {"a": [sys.executable, "-c", "print('ok')"]}})
            result = verify_acceptance(store, task, "a"*40, cwd=tmp)
            self.assertEqual(result["status"], "pending")

    def test_acceptance_records_evidence_bound_to_head(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            store = init_store(base)
            task = {"task_id": "TASK-T", "acceptance_criteria": ["a"]}
            write_json(store / "config.json",
                       {"acceptance_commands": {"a": [sys.executable, "-c", "print('ok')"]}})
            result = verify_acceptance(store, task, "a"*40, cwd=tmp)
            self.assertEqual(result["status"], "passed")
            saved = read_json(store / "tasks/TASK-T.json")
            self.assertEqual(saved["acceptance_revision"], "a"*40)
            self.assertEqual(saved["acceptance_results"]["a"]["status"], "PASS")

    def test_failed_criterion_never_becomes_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            store = init_store(base)
            task = {"task_id": "TASK-T", "acceptance_criteria": ["a"]}
            write_json(store / "config.json",
                       {"acceptance_commands": {"a": [sys.executable, "-c", "raise SystemExit(4)"]}})
            result = verify_acceptance(store, task, "a"*40, cwd=tmp)
            self.assertEqual(result["status"], "failed")
            self.assertFalse((store / "tasks/TASK-T.json").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
