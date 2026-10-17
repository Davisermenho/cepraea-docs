#!/usr/bin/env python3
"""Tests for the event and evidence modules."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.store import init_store, read_jsonl
from espaut.events import log_event, make_event, make_evidence, save_evidence


def test_make_event() -> dict[str, str]:
    ev = make_event("task_created", task_id="TSK-001", actor="user")
    return {
        "has_event_id": "PASS" if ev["event_id"].startswith("EVT-") else "FAIL",
        "has_timestamp": "PASS" if "occurred_at" in ev else "FAIL",
        "event_type": "PASS" if ev["event_type"] == "task_created" else "FAIL",
        "task_id": "PASS" if ev["task_id"] == "TSK-001" else "FAIL",
        "actor": "PASS" if ev["actor"] == "user" else "FAIL",
        "no_none_keys": "PASS" if all(v is not None for v in ev.values()) else "FAIL",
    }


def test_make_event_minimal() -> dict[str, str]:
    ev = make_event("status_check")
    return {
        "no_task_id": "PASS" if "task_id" not in ev else "FAIL",
        "default_actor": "PASS" if ev["actor"] == "espaut" else "FAIL",
    }


def test_log_event_persists() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        log_event(store, "first_event", task_id="TSK-A")
        log_event(store, "second_event", task_id="TSK-A")
        records = read_jsonl(store / "events.jsonl")
        return {
            "count": "PASS" if len(records) == 2 else "FAIL",
            "first_type": "PASS" if records[0]["event_type"] == "first_event" else "FAIL",
            "second_type": "PASS" if records[1]["event_type"] == "second_event" else "FAIL",
        }


def test_make_evidence() -> dict[str, str]:
    ev = make_evidence(
        "git",
        "abc123",
        "commit verified on remote",
        task_id="TSK-001",
        related_revision="abc123",
    )
    return {
        "has_evidence_id": "PASS" if ev["evidence_id"].startswith("EVD-") else "FAIL",
        "has_integrity": "PASS" if "integrity_sha256" in ev else "FAIL",
        "has_timestamp": "PASS" if "observed_at" in ev else "FAIL",
        "source_system": "PASS" if ev["source_system"] == "git" else "FAIL",
    }


def test_evidence_integrity() -> dict[str, str]:
    ev = make_evidence("github", "PR#42", "checks passed")
    integrity = ev.pop("integrity_sha256")
    import hashlib
    canonical = json.dumps(ev, ensure_ascii=False, sort_keys=True)
    expected = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return {
        "integrity_matches": "PASS" if integrity == expected else "FAIL",
    }


def test_save_evidence() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        ev = make_evidence("git", "def456", "push confirmed")
        path = save_evidence(store, ev)
        return {
            "file_exists": "PASS" if path.exists() else "FAIL",
            "in_evidence_dir": "PASS" if path.parent.name == "evidence" else "FAIL",
            "content_matches": (
                "PASS"
                if json.loads(path.read_text(encoding="utf-8"))["evidence_id"]
                == ev["evidence_id"]
                else "FAIL"
            ),
        }


ALL_TESTS = [
    ("make_event", test_make_event),
    ("make_event_minimal", test_make_event_minimal),
    ("log_event_persists", test_log_event_persists),
    ("make_evidence", test_make_evidence),
    ("evidence_integrity", test_evidence_integrity),
    ("save_evidence", test_save_evidence),
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

    print(f"\nevents: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
