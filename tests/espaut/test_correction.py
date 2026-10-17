#!/usr/bin/env python3
"""Tests for correction cycle."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.correction import (
    can_attempt_correction,
    check_scope_compliance,
    make_attempt,
    make_diagnosis,
    record_attempt_result,
    run_correction_check,
)
from espaut.store import init_store


def test_make_diagnosis() -> dict[str, str]:
    d = make_diagnosis("PND-001", "null pointer in handler", source="human")
    return {
        "has_id": "PASS" if d["diagnosis_id"].startswith("DGN-") else "FAIL",
        "pendency": "PASS" if d["pendency_id"] == "PND-001" else "FAIL",
        "source": "PASS" if d["diagnosis_source"] == "human" else "FAIL",
    }


def test_make_attempt() -> dict[str, str]:
    a = make_attempt("PND-001", 1, input_revision="abc123", proposed_changes=["main.py"])
    return {
        "has_id": "PASS" if a["attempt_id"].startswith("ATT-") else "FAIL",
        "number": "PASS" if a["attempt_number"] == 1 else "FAIL",
        "state": "PASS" if a["attempt_state"] == "INICIADA" else "FAIL",
    }


def test_record_result() -> dict[str, str]:
    a = make_attempt("PND-001", 1)
    updated = record_attempt_result(
        a,
        applied_changes=["main.py"],
        output_revision="def456",
        validation_result="PASS",
    )
    return {
        "applied": "PASS" if updated["applied_changes"] == ["main.py"] else "FAIL",
        "revision": "PASS" if updated["output_revision"] == "def456" else "FAIL",
        "state": "PASS" if updated["attempt_state"] == "CONCLUIDA" else "FAIL",
    }


def test_can_attempt_within_limit() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        ok, _ = can_attempt_correction(store, "PND-001", [])
        return {"first_ok": "PASS" if ok else "FAIL"}


def test_can_attempt_at_limit() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        attempts = [
            {"attempt_state": "FALHA", "proposed_changes": ["a.py"]},
            {"attempt_state": "FALHA", "proposed_changes": ["a.py"]},
            {"attempt_state": "FALHA", "proposed_changes": ["a.py"]},
        ]
        ok, reason = can_attempt_correction(store, "PND-001", attempts)
        return {"blocked": "PASS" if not ok else "FAIL"}


def test_run_correction_check_allowed() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        result = run_correction_check(store, "TASK-001", "PND-001", [])
        return {"allowed": "PASS" if result["status"] == "allowed" else "FAIL"}


def test_run_correction_check_blocked() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        attempts = [{"attempt_state": "FALHA", "proposed_changes": []} for _ in range(3)]
        result = run_correction_check(store, "TASK-001", "PND-001", attempts)
        return {"blocked": "PASS" if result["status"] == "blocked" else "FAIL"}


def test_scope_compliance() -> dict[str, str]:
    ok, out = check_scope_compliance(["src/main.py", "src/util.py"], ["src/*"])
    fail, out2 = check_scope_compliance(["src/main.py", "config.yaml"], ["src/*"])
    no_scope, _ = check_scope_compliance(["anything.py"], [])
    return {
        "in_scope": "PASS" if ok else "FAIL",
        "out_of_scope": "PASS" if not fail and "config.yaml" in out2 else "FAIL",
        "no_scope_ok": "PASS" if no_scope else "FAIL",
    }


ALL_TESTS = [
    ("make_diagnosis", test_make_diagnosis),
    ("make_attempt", test_make_attempt),
    ("record_result", test_record_result),
    ("can_attempt_within_limit", test_can_attempt_within_limit),
    ("can_attempt_at_limit", test_can_attempt_at_limit),
    ("correction_check_allowed", test_run_correction_check_allowed),
    ("correction_check_blocked", test_run_correction_check_blocked),
    ("scope_compliance", test_scope_compliance),
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

    print(f"\ncorrection: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
