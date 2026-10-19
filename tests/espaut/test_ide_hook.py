#!/usr/bin/env python3
"""Unit tests for project-local VS Code hooks; no external Git calls."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from espaut import ide_hook
from espaut.store import init_store, write_json


class IdeHookTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.store = init_store(self.root)
        self.session = {"cwd": str(self.root), "session_id": "vs-code-chat"}
        write_json(self.store / "config.json", {
            "auto_commit": True, "eligible_patterns": ["*.py"],
            "auto_pr": True, "auto_merge": False,
        })
        write_json(self.store / "tasks" / "TASK-001.json", {
            "task_id": "TASK-001", "branch_name": "feature/chat",
            "state": "EM_EXECUCAO",
        })
        self.root_patch = patch.object(ide_hook, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def test_pre_and_post_pair_by_same_session_without_turn_id(self):
        with patch.object(ide_hook, "dirty_paths", side_effect=[set(), {"new.py"}]), \
             patch.object(ide_hook, "git", return_value="feature/chat"), \
             patch("espaut.stop_worker.launch_worker", return_value=True) as launch:
            self.assertEqual(ide_hook.run_hook("pre", self.session), "")
            msg = ide_hook.run_hook("post", {**self.session, "turn_id": "stop-only"})
            self.assertIn("queued", msg)
            launch.assert_called_once_with(self.store, "TASK-001", str(self.root),
                                           preserve_changes=True)

    def test_preexisting_dirty_work_is_not_committed(self):
        with patch.object(ide_hook, "dirty_paths", side_effect=[{"existing.py"}, {"existing.py", "new.py"}]), \
             patch.object(ide_hook, "git", return_value="feature/chat"), \
             patch("espaut.stop_worker.launch_worker") as launch:
            ide_hook.run_hook("pre", self.session)
            msg = ide_hook.run_hook("post", self.session)
            self.assertIn("pre-existing", msg)
            launch.assert_not_called()

    def test_excluded_preexisting_bytecode_does_not_block_new_eligible_file(self):
        write_json(self.store / "config.json", {
            "auto_commit": True,
            "eligible_patterns": ["new.py"],
            "auto_pr": False,
            "auto_merge": False,
        })
        excluded = {"espaut/__pycache__/cli.cpython-312.pyc", "old-untracked.txt"}
        with patch.object(ide_hook, "dirty_paths",
                          side_effect=[excluded, excluded | {"new.py"}]), \
             patch.object(ide_hook, "git", return_value="feature/chat"), \
             patch("espaut.stop_worker.launch_worker", return_value=True) as launch:
            self.assertEqual(ide_hook.run_hook("pre", self.session), "")
            message = ide_hook.run_hook("post", self.session)
            self.assertIn("queued", message)
            launch.assert_called_once_with(self.store, "TASK-001", str(self.root),
                                           preserve_changes=True)

    def test_excluded_files_alone_do_not_trigger_a_commit(self):
        excluded = {"espaut/__pycache__/cli.cpython-312.pyc"}
        with patch.object(ide_hook, "dirty_paths", side_effect=[excluded, excluded]), \
             patch("espaut.stop_worker.launch_worker") as launch:
            ide_hook.run_hook("pre", self.session)
            message = ide_hook.run_hook("post", self.session)
            self.assertIn("no new eligible", message)
            launch.assert_not_called()

    def test_duplicate_active_tasks_are_not_arbitrarily_selected(self):
        write_json(self.store / "tasks" / "TASK-002.json", {
            "task_id": "TASK-002", "branch_name": "feature/chat",
            "state": "EM_EXECUCAO",
        })
        with patch.object(ide_hook, "dirty_paths", side_effect=[set(), {"new.py"}]), \
             patch.object(ide_hook, "git", return_value="feature/chat"), \
             patch("espaut.stop_worker.launch_worker") as launch:
            ide_hook.run_hook("pre", self.session)
            message = ide_hook.run_hook("post", self.session)
            self.assertIn("one active task", message)
            launch.assert_not_called()

    def test_project_mismatch_is_not_processed(self):
        with patch.object(ide_hook, "dirty_paths") as dirty:
            message = ide_hook.run_hook("post", {"cwd": str(self.root.parent),
                                                 "session_id": "other"})
            self.assertIn("another project", message)
            dirty.assert_not_called()

    def test_missing_project_policy_cannot_start_worker(self):
        (self.store / "config.json").unlink()
        with patch("espaut.stop_worker.launch_worker") as launch:
            self.assertIn("no authorized", ide_hook.run_hook("post", self.session))
            launch.assert_not_called()

    def test_protected_branch_cannot_start_worker(self):
        with patch.object(ide_hook, "dirty_paths", return_value=set()), \
             patch.object(ide_hook, "git", return_value="main"), \
             patch("espaut.stop_worker.launch_worker") as launch:
            self.assertIn("protected", ide_hook.run_hook("post", self.session))
            launch.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
