#!/usr/bin/env python3
"""Run explicitly configured criterion-specific acceptance tests for a Git HEAD.

A passing generic test command does not approve unrelated criteria. Every
criterion must name its own command, pass, and bind evidence to this revision.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from espaut.store import load_config, write_json


def verify_acceptance(store: Path, task: dict, revision: str, *, cwd: str) -> dict:
    criteria = task.get("acceptance_criteria") or []
    if not criteria:
        return {"status": "pending", "reason": "acceptance criteria absent"}
    current = task.get("acceptance_results") or {}
    if task.get("acceptance_revision") == revision and all(
        isinstance(current.get(str(c)), dict)
        and current[str(c)].get("status") == "PASS"
        and current[str(c)].get("revision") == revision
        and current[str(c)].get("evidence_reference")
        for c in criteria
    ):
        return {"status": "passed", "revision": revision, "cached": True}
    cfg = load_config(store)
    commands = cfg.get("acceptance_commands", {})
    if not isinstance(commands, dict):
        return {"status": "pending", "reason": "invalid acceptance_commands"}
    results = {}
    for criterion in criteria:
        key = str(criterion)
        argv = commands.get(key)
        if not isinstance(argv, list) or not argv or not all(isinstance(x, str) and x for x in argv):
            return {"status": "pending", "reason": f"missing configured test for {key}"}
        try:
            proc = subprocess.run(argv, cwd=cwd, text=True, capture_output=True,
                                  timeout=cfg.get("acceptance_timeout_seconds", 120),
                                  check=False)
        except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
            return {"status": "failed", "reason": f"{key}: {type(exc).__name__}"}
        observation = (proc.stdout or "") + "\n" + (proc.stderr or "")
        fingerprint = hashlib.sha256(observation.encode("utf-8")).hexdigest()
        evidence_id = hashlib.sha256((revision+"|"+key+"|"+fingerprint).encode()).hexdigest()
        proof = {"criterion": key, "revision": revision, "returncode": proc.returncode,
                 "output_sha256": fingerprint, "evidence_id": evidence_id}
        write_json(store / "evidence" / f"acceptance-{evidence_id}.json", proof)
        if proc.returncode != 0:
            return {"status": "failed", "criterion": key, "evidence_reference": evidence_id,
                    "reason": f"configured acceptance test failed (exit {proc.returncode})"}
        results[key] = {"status": "PASS", "revision": revision,
                        "evidence_reference": f"acceptance-{evidence_id}.json"}
    # Only publish results after ALL criterion-specific commands succeeded.
    task["acceptance_revision"] = revision
    task["acceptance_results"] = results
    write_json(store / "tasks" / f"{task['task_id']}.json", task)
    return {"status": "passed", "revision": revision, "count": len(results)}
