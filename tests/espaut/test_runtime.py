#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from espaut.runtime import (
    RuntimeDeploymentError,
    _run_validation,
    deploy_and_install,
    _verify_source_revision,
    deploy_runtime,
    hook_command,
    install_hook_config,
    rollback_runtime,
    runtime_status,
)
from espaut import runtime_hook
from espaut.gh_ops import pr_view_json, repository_info
from espaut.git_ops import repository_slug
from espaut.governance import check_c7_authority


class RuntimeDeploymentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.runtime = self.root / "runtime"
        self.validation = [sys.executable, "-B", "-c", "import espaut"]
        self.revision = patch("espaut.runtime._verify_source_revision")
        self.revision.start()

    def tearDown(self):
        self.revision.stop()
        self.temp.cleanup()

    def test_atomic_update_integrity_and_rollback(self):
        first = deploy_runtime(
            REPO, self.runtime, implementation_sha="a" * 40,
            validation_command=self.validation,
        )
        self.assertEqual(first["status"], "activated")
        first_target = (self.runtime / "current").resolve()
        second = deploy_runtime(
            REPO, self.runtime, implementation_sha="b" * 40,
            validation_command=self.validation,
        )
        self.assertEqual(second["status"], "activated")
        self.assertNotEqual(first_target, (self.runtime / "current").resolve())
        rolled = rollback_runtime(self.runtime)
        self.assertEqual(rolled["status"], "rolled_back")
        self.assertEqual(first_target, (self.runtime / "current").resolve())
        self.assertEqual(runtime_status(self.runtime)["integrity"], "verified")

    def test_hook_install_preserves_third_party_and_replaces_only_espaut(self):
        deploy_runtime(
            REPO, self.runtime, implementation_sha="c" * 40,
            validation_command=self.validation,
        )
        config_path = self.root / "settings.json"
        third_party = "/opt/vendor/trace-hook"
        config_path.write_text(json.dumps({
            "env": {"KEEP": "yes"},
            "hooks": {
                "UserPromptSubmit": [
                    {"hooks": [{"type": "command", "command": third_party}]},
                    {"hooks": [{"type": "command", "command": "/tmp/ESPAUT-GLOBAL-HOOKS/hook_bridge.py pre"}]},
                ],
                "Stop": [{"hooks": [{"type": "command", "command": third_party}]}],
            },
        }), encoding="utf-8")
        report = install_hook_config(config_path, self.runtime, "claude")
        self.assertEqual(report["removed"], 1)
        installed = json.loads(config_path.read_text(encoding="utf-8"))
        rendered = json.dumps(installed)
        commands = [
            handler["command"]
            for groups in installed["hooks"].values()
            for group in groups
            for handler in group.get("hooks", [])
            if isinstance(handler, dict) and "command" in handler
        ]
        self.assertIn(third_party, rendered)
        self.assertEqual(installed["env"], {"KEEP": "yes"})
        self.assertNotIn("ESPAUT-GLOBAL-HOOKS", rendered)
        self.assertIn(hook_command(self.runtime, "claude", "pre"), commands)
        self.assertIn(hook_command(self.runtime, "claude", "post"), commands)
        self.assertTrue(Path(report["backup"]).is_file())

    def test_source_revision_verification_rejects_mismatch_and_dirty_tree(self):
        repo = self.root / "source"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
        subprocess.run(["git", "config", "user.name", "ESPAUT Test"], cwd=repo, check=True)
        (repo / "file.txt").write_text("one\n", encoding="utf-8")
        subprocess.run(["git", "add", "file.txt"], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-qm", "one"], cwd=repo, check=True)
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
        with self.assertRaises(RuntimeDeploymentError):
            _verify_source_revision(repo, "f" * 40)
        _verify_source_revision(repo, sha)
        (repo / "file.txt").write_text("dirty\n", encoding="utf-8")
        with self.assertRaises(RuntimeDeploymentError):
            _verify_source_revision(repo, sha)

    def test_default_validation_runs_each_test_file_like_ci(self):
        tests = self.root / "source" / "tests" / "espaut"
        tests.mkdir(parents=True)
        (tests / "test_a.py").write_text("print('A')\n", encoding="utf-8")
        (tests / "test_b.py").write_text("print('B')\n", encoding="utf-8")
        result = _run_validation(self.root / "source", None)
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(len(result["commands"]), 2)

    def test_default_validation_stops_on_first_failure(self):
        tests = self.root / "source" / "tests" / "espaut"
        tests.mkdir(parents=True)
        (tests / "test_a.py").write_text("raise SystemExit(7)\n", encoding="utf-8")
        (tests / "test_b.py").write_text("print('must not run')\n", encoding="utf-8")
        result = _run_validation(self.root / "source", None)
        self.assertEqual(result["exit_code"], 7)

    def test_hook_install_failure_restores_config_and_active_release(self):
        first = deploy_runtime(
            REPO, self.runtime, implementation_sha="d" * 40,
            validation_command=self.validation,
        )
        old_target = (self.runtime / "current").resolve()
        config = self.root / "settings.json"
        original = b'{"third_party":true}\n'
        config.write_bytes(original)
        def fake_deploy(*args, **kwargs):
            replacement = self.runtime / "versions" / "new"
            replacement.mkdir()
            current = self.runtime / "current"
            current.unlink()
            current.symlink_to(Path("versions") / "new")
            return {"status": "activated", "release": "new"}

        with patch("espaut.runtime.deploy_runtime", side_effect=fake_deploy), \
                patch("espaut.runtime.install_hook_config", side_effect=OSError("write failed")):
            with self.assertRaises(OSError):
                deploy_and_install(
                    REPO, self.runtime, implementation_sha="e" * 40,
                    hook_configs={"claude": config},
                )
        self.assertEqual(config.read_bytes(), original)
        self.assertEqual((self.runtime / "current").resolve(), old_target)
        self.assertEqual(first["release"], runtime_status(self.runtime)["release"])

    def test_runtime_status_parses_escaped_json_hook_commands(self):
        deploy_runtime(
            REPO, self.runtime, implementation_sha="f" * 40,
            validation_command=self.validation,
        )
        config = self.root / "hooks.json"
        install_hook_config(config, self.runtime, "codex")
        status = runtime_status(self.runtime, {"codex": config})
        self.assertEqual(status["status"], "active")
        self.assertTrue(status["hooks"]["codex"])


class RuntimeHookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / "project"
        self.project.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "feature/runtime"], cwd=self.project, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.project, check=True)
        subprocess.run(["git", "config", "user.name", "ESPAUT Test"], cwd=self.project, check=True)
        (self.project / "README.md").write_text("baseline\n", encoding="utf-8")
        subprocess.run(["git", "add", "README.md"], cwd=self.project, check=True)
        subprocess.run(["git", "commit", "-qm", "baseline"], cwd=self.project, check=True)
        store = self.project / ".espaut"
        (store / "tasks").mkdir(parents=True)
        (store / "config.json").write_text(json.dumps({
            "auto_commit": False,
            "eligible_patterns": ["*.py"],
            "policy_version": "test",
        }), encoding="utf-8")
        self.runtime = self.root / "runtime"
        (self.runtime / "state").mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def test_duplicate_pre_event_is_suppressed_and_metadata_is_provider_specific(self):
        payload = {
            "cwd": str(self.project), "session_id": "session-1",
            "hook_event_name": "UserPromptSubmit", "prompt": "same prompt",
        }
        with patch.object(runtime_hook, "_runtime_root", return_value=self.runtime):
            _, first = runtime_hook.dispatch("codex", "pre", payload)
            _, second = runtime_hook.dispatch("codex", "pre", payload)
        self.assertEqual(first["outcome"], "snapshot")
        self.assertEqual(first["provider"], "codex")
        self.assertEqual(first["session_id"], "session-1")
        self.assertEqual(second["outcome"], "duplicate_suppressed")

    def test_missing_session_fails_closed(self):
        payload = {"cwd": str(self.project), "hook_event_name": "Stop"}
        with patch.object(runtime_hook, "_runtime_root", return_value=self.runtime):
            message, record = runtime_hook.dispatch("claude", "post", payload)
        self.assertEqual(record["outcome"], "session_missing")
        self.assertIn("sessão", message)

    def test_project_hook_is_detected_as_live_dependency(self):
        local = self.project / ".codex" / "hooks.json"
        local.parent.mkdir()
        local.write_text('{"hooks":{"Stop":[{"hooks":[{"command":"python espaut/ide_hook.py post"}]}]}}')
        payload = {"cwd": str(self.project), "session_id": "s", "hook_event_name": "Stop"}
        with patch.object(runtime_hook, "_runtime_root", return_value=self.runtime):
            _, record = runtime_hook.dispatch("codex", "post", payload)
        self.assertEqual(record["outcome"], "delegated_to_project_hook")

    def test_auto_task_is_created_once_and_reused(self):
        config_path = self.project / ".espaut" / "config.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["auto_task"] = True
        config_path.write_text(json.dumps(config), encoding="utf-8")
        first_payload = {
            "cwd": str(self.project), "session_id": "auto-session",
            "turn_id": "turn-1", "hook_event_name": "UserPromptSubmit",
        }
        second_payload = {**first_payload, "turn_id": "turn-2"}
        with patch.object(runtime_hook, "_runtime_root", return_value=self.runtime):
            _, first = runtime_hook.dispatch("codex", "pre", first_payload)
            _, second = runtime_hook.dispatch("codex", "pre", second_payload)
        tasks = list((self.project / ".espaut" / "tasks").glob("TASK-*.json"))
        self.assertEqual(first["outcome"], "task_created_snapshot")
        self.assertEqual(second["outcome"], "snapshot")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(first["task_id"], second["task_id"])


class ExplicitGitHubIdentityTests(unittest.TestCase):
    def test_pr_query_passes_explicit_repository(self):
        response = subprocess.CompletedProcess(
            [], 0, stdout='{"number":2,"state":"OPEN"}', stderr="",
        )
        with patch("espaut.gh_ops.run_gh", return_value=response) as run:
            result = pr_view_json(2, repository="Davisermenho/cepraea-docs")
        self.assertEqual(result["number"], 2)
        self.assertIn("--repo", run.call_args.args)
        self.assertIn("Davisermenho/cepraea-docs", run.call_args.args)

    def test_repository_permission_is_bound_to_expected_identity(self):
        response = subprocess.CompletedProcess(
            [], 0,
            stdout='{"nameWithOwner":"Davisermenho/cepraea-docs","viewerPermission":"READ"}',
            stderr="",
        )
        with patch("espaut.gh_ops.run_gh", return_value=response):
            info = repository_info("Davisermenho/cepraea-docs")
        self.assertEqual(info["viewerPermission"], "READ")

    def test_c7_never_passes_with_read_only_github_identity(self):
        result = check_c7_authority(
            {"task_id": "TASK-1"}, [], automatic_policy=True,
            technical_permission="READ", repository_authorized=True,
        )
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("READ", result["detail"])

    def test_repository_slug_discards_transport_and_credentials(self):
        with patch("espaut.git_ops.run_git") as run:
            run.return_value = subprocess.CompletedProcess(
                [], 0, stdout="https://token@example.invalid/owner/repo.git\n", stderr="",
            )
            self.assertEqual(repository_slug(), "owner/repo")


if __name__ == "__main__":
    unittest.main()
