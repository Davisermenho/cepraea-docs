#!/usr/bin/env python3
"""Tests for CI/check monitoring."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.checks import (
    CheckState,
    compute_aggregate,
    make_check_record,
    normalize_check_state,
    query_checks,
)
from espaut.store import init_store


def test_normalize_success() -> dict[str, str]:
    cases = [
        ({"state": "SUCCESS", "conclusion": ""}, CheckState.APROVADO),
        ({"state": "", "conclusion": "success"}, CheckState.APROVADO),
        ({"state": "NEUTRAL", "conclusion": ""}, CheckState.APROVADO),
    ]
    checks: dict[str, str] = {}
    for i, (raw, expected) in enumerate(cases):
        result = normalize_check_state(raw)
        checks[f"success_{i}"] = "PASS" if result == expected else f"FAIL: {result}"
    return checks


def test_normalize_failure() -> dict[str, str]:
    cases = [
        ({"state": "FAILURE", "conclusion": ""}, CheckState.REPROVADO),
        ({"state": "", "conclusion": "failure"}, CheckState.REPROVADO),
        ({"state": "TIMED_OUT", "conclusion": ""}, CheckState.REPROVADO),
    ]
    checks: dict[str, str] = {}
    for i, (raw, expected) in enumerate(cases):
        result = normalize_check_state(raw)
        checks[f"failure_{i}"] = "PASS" if result == expected else f"FAIL: {result}"
    return checks


def test_normalize_pending() -> dict[str, str]:
    result = normalize_check_state({"state": "PENDING", "conclusion": ""})
    return {"pending": "PASS" if result == CheckState.PENDENTE else "FAIL"}


def test_normalize_cancelled() -> dict[str, str]:
    result = normalize_check_state({"state": "CANCELLED", "conclusion": ""})
    return {"cancelled": "PASS" if result == CheckState.CANCELADO else "FAIL"}


def test_normalize_unknown() -> dict[str, str]:
    result = normalize_check_state({"state": "WEIRD", "conclusion": "bizarre"})
    return {"unknown": "PASS" if result == CheckState.INDETERMINADO else "FAIL"}


def test_make_check_record() -> dict[str, str]:
    raw = {
        "name": "ci/build",
        "state": "SUCCESS",
        "conclusion": "",
        "detailsUrl": "https://ci.example.com/1",
        "startedAt": "2026-10-17T10:00:00Z",
        "completedAt": "2026-10-17T10:05:00Z",
    }
    record = make_check_record(raw, pr_number=42, evaluated_revision="abc123")
    return {
        "name": "PASS" if record["name"] == "ci/build" else "FAIL",
        "normalized": "PASS" if record["normalized_result"] == "APROVADO" else "FAIL",
        "revision": "PASS" if record["evaluated_revision"] == "abc123" else "FAIL",
        "pr": "PASS" if record["pr_number"] == 42 else "FAIL",
    }


def test_aggregate_all_pass() -> dict[str, str]:
    checks = [
        {"normalized_result": "APROVADO"},
        {"normalized_result": "APROVADO"},
        {"normalized_result": "IGNORADO"},
    ]
    result = compute_aggregate(checks)
    return {"all_pass": "PASS" if result == CheckState.APROVADO else "FAIL"}


def test_aggregate_one_fail() -> dict[str, str]:
    checks = [
        {"normalized_result": "APROVADO"},
        {"normalized_result": "REPROVADO"},
    ]
    result = compute_aggregate(checks)
    return {"one_fail": "PASS" if result == CheckState.REPROVADO else "FAIL"}


def test_aggregate_pending() -> dict[str, str]:
    checks = [
        {"normalized_result": "APROVADO"},
        {"normalized_result": "PENDENTE"},
    ]
    result = compute_aggregate(checks)
    return {"pending": "PASS" if result == CheckState.PENDENTE else "FAIL"}


def test_aggregate_empty() -> dict[str, str]:
    result = compute_aggregate([])
    return {"empty": "PASS" if result == CheckState.NAO_CONFIGURADO else "FAIL"}


def test_query_no_checks() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        with patch("espaut.checks.pr_checks_json", return_value=[]):
            result = query_checks(store, "TASK-001", 42, "abc123")
            return {
                "not_configured": "PASS" if result["aggregate"] == "NAO_CONFIGURADO" else "FAIL",
            }


def test_query_with_checks() -> dict[str, str]:
    raw = [
        {"name": "build", "state": "SUCCESS", "conclusion": "", "detailsUrl": "", "startedAt": None, "completedAt": None},
        {"name": "lint", "state": "FAILURE", "conclusion": "", "detailsUrl": "", "startedAt": None, "completedAt": None},
    ]
    with tempfile.TemporaryDirectory() as tmp:
        store = init_store(Path(tmp))
        with patch("espaut.checks.pr_checks_json", return_value=raw):
            result = query_checks(store, "TASK-001", 42, "abc123")
            return {
                "queried": "PASS" if result["status"] == "queried" else "FAIL",
                "count": "PASS" if len(result["checks"]) == 2 else "FAIL",
                "aggregate_fail": "PASS" if result["aggregate"] == "REPROVADO" else "FAIL",
            }


ALL_TESTS = [
    ("normalize_success", test_normalize_success),
    ("normalize_failure", test_normalize_failure),
    ("normalize_pending", test_normalize_pending),
    ("normalize_cancelled", test_normalize_cancelled),
    ("normalize_unknown", test_normalize_unknown),
    ("make_check_record", test_make_check_record),
    ("aggregate_all_pass", test_aggregate_all_pass),
    ("aggregate_one_fail", test_aggregate_one_fail),
    ("aggregate_pending", test_aggregate_pending),
    ("aggregate_empty", test_aggregate_empty),
    ("query_no_checks", test_query_no_checks),
    ("query_with_checks", test_query_with_checks),
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

    print(f"\nchecks: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
