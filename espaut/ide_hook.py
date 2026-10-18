#!/usr/bin/env python3
"""Project-scoped Claude Code / Codex Stop hook for VS Code (WSL/Linux).

The hook runs the ESPAUT package in the SAME Git checkout as this file.
It does not rely on temporary NotebookLM/runs clones. Git operations are
performed by the Python worker after Stop, never by the coding agent.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def git(*args: str) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(ROOT), *args],
                                capture_output=True, text=True, timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def dirty_paths() -> set[str] | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
            capture_output=True, timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode:
        return None
    records = result.stdout.split(b"\x00")
    paths: set[str] = set()
    index = 0
    while index < len(records):
        entry = records[index]
        index += 1
        if not entry or len(entry) < 4:
            continue
        paths.add(os.fsdecode(entry[3:]))
        if (b"R" in entry[:2] or b"C" in entry[:2]) and index < len(records):
            paths.add(os.fsdecode(records[index]))
            index += 1
    return paths


def find_task(store: Path, branch: str) -> dict | None:
    candidates = []
    for path in sorted((store / "tasks").glob("TASK-*.json")):
        try:
            task = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if (task.get("branch_name") == branch
                and task.get("state") not in ("INTEGRADA", "ENCERRADA_SEM_MERGE", "INTERROMPIDA")):
            candidates.append(task)
    return candidates[0] if len(candidates) == 1 else None


def run_hook(phase: str, payload: dict) -> str:
    # Never act on another checkout, even when multiple projects are open.
    cwd = payload.get("cwd")
    if not isinstance(cwd, str) or not Path(cwd).is_dir():
        return "ESPAUT: hook did not receive a valid project directory."
    try:
        actual = Path(cwd).resolve()
    except OSError:
        return "ESPAUT: project directory unavailable."
    if actual != ROOT and ROOT not in actual.parents:
        return "ESPAUT: ignored event from another project."
    store = ROOT / ".espaut"
    cfg_path = store / "config.json"
    if not cfg_path.is_file():
        return "ESPAUT: project has no authorized .espaut/config.json."
    from espaut.store import load_config
    cfg = load_config(store)
    status = dirty_paths()
    if status is None:
        return "ESPAUT: cannot verify working tree; automatic actions blocked."
    session = str(payload.get("session_id") or "session-unknown")
    turn = str(payload.get("turn_id") or "")
    key = hashlib.sha256((session + "|" + turn).encode()).hexdigest()[:32]
    snapshot = store / "cache" / "ide-hooks" / (key + ".json")
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    if phase == "pre":
        snapshot.write_text(json.dumps({"root": str(ROOT), "dirty": sorted(status)}),
                            encoding="utf-8")
        return ""
    if phase != "post":
        return ""
    if cfg.get("auto_commit") is not True or not cfg.get("eligible_patterns"):
        return "ESPAUT: automatic preservation is not enabled by project policy."
    previous: dict = {}
    if snapshot.exists():
        try:
            previous = json.loads(snapshot.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return "ESPAUT: invalid pre-task snapshot; no action."
    if status and (not previous or previous.get("root") != str(ROOT)):
        return "ESPAUT: missing pre-task snapshot; unsafe to commit."
    if status and set(previous.get("dirty", [])):
        return "ESPAUT: pre-existing uncommitted work; automatic commit blocked."
    branch = git("branch", "--show-current")
    if not branch or branch in ("main", "master"):
        return "ESPAUT: protected/default branch; no Git changes."
    task = find_task(store, branch)
    if task is None:
        return "ESPAUT: one active task associated with this branch is required."
    from espaut.stop_worker import launch_worker
    if not launch_worker(store, task["task_id"], str(ROOT), preserve_changes=bool(status)):
        return "ESPAUT: worker not started; inspect project policy."
    return "ESPAUT: automatic Git/GitHub lifecycle queued."


def main() -> int:
    phase = sys.argv[1] if len(sys.argv) > 1 else ""
    if phase not in ("pre", "post"):
        return 2
    try:
        payload = json.loads(sys.stdin.buffer.read(262144))
        if not isinstance(payload, dict):
            payload = {}
    except (OSError, ValueError):
        payload = {}
    try:
        message = run_hook(phase, payload)
    except Exception as exc:
        message = f"ESPAUT: hook failed ({type(exc).__name__}); no success claimed."
    if phase == "post":
        response: dict = {"continue": True}
        if message:
            response["systemMessage"] = message
        print(json.dumps(response))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
