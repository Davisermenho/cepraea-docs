#!/usr/bin/env python3
"""Diagnosis, correction attempts, and re-verification (CTX-06)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from espaut.events import log_event, make_evidence, save_evidence
from espaut.store import load_config, new_id, write_json


def make_diagnosis(
    pendency_id: str,
    suspected_cause: str,
    *,
    evidence_references: list[str] | None = None,
    proposed_intervention: str = "",
    scope_impact: list[str] | None = None,
    uncertainties: str = "",
    source: str = "human",
) -> dict[str, Any]:
    """Build a diagnosis record."""
    return {
        "diagnosis_id": new_id("DGN-"),
        "pendency_id": pendency_id,
        "evidence_references": evidence_references or [],
        "suspected_cause": suspected_cause,
        "proposed_intervention": proposed_intervention,
        "scope_impact": scope_impact or [],
        "uncertainties": uncertainties,
        "diagnosis_source": source,
    }


def make_attempt(
    pendency_id: str,
    attempt_number: int,
    *,
    input_revision: str | None = None,
    proposed_changes: list[str] | None = None,
) -> dict[str, Any]:
    """Build a correction attempt record."""
    return {
        "attempt_id": new_id("ATT-"),
        "pendency_id": pendency_id,
        "attempt_number": attempt_number,
        "input_revision": input_revision,
        "proposed_changes": proposed_changes or [],
        "applied_changes": [],
        "output_revision": None,
        "validation_result": None,
        "attempt_state": "INICIADA",
    }


def can_attempt_correction(
    store: Path,
    pendency_id: str,
    previous_attempts: list[dict[str, Any]],
) -> tuple[bool, str]:
    """Check whether another correction attempt is allowed."""
    config = load_config(store)
    max_attempts = config.get("correction_max_attempts", 3)

    if len(previous_attempts) >= max_attempts:
        return False, f"limit reached: {len(previous_attempts)}/{max_attempts}"

    failed = [a for a in previous_attempts if a.get("attempt_state") == "FALHA"]
    if len(failed) >= max_attempts:
        return False, f"all {len(failed)} attempts failed"

    last = previous_attempts[-1] if previous_attempts else None
    if last and last.get("attempt_state") == "FALHA":
        last_changes = set(last.get("proposed_changes", []))
        if last_changes:
            return True, "previous attempt failed; new evidence may justify retry"

    return True, "attempt allowed"


def record_attempt_result(
    attempt: dict[str, Any],
    *,
    applied_changes: list[str],
    output_revision: str | None = None,
    validation_result: str | None = None,
    state: str = "CONCLUIDA",
) -> dict[str, Any]:
    """Update an attempt record with its result."""
    attempt["applied_changes"] = applied_changes
    attempt["output_revision"] = output_revision
    attempt["validation_result"] = validation_result
    attempt["attempt_state"] = state
    return attempt


def run_correction_check(
    store: Path,
    task_id: str,
    pendency_id: str,
    previous_attempts: list[dict[str, Any]],
) -> dict[str, Any]:
    """Pre-flight check before starting a correction attempt.

    Returns a report indicating whether correction can proceed.
    """
    allowed, reason = can_attempt_correction(store, pendency_id, previous_attempts)
    attempt_number = len(previous_attempts) + 1

    if not allowed:
        log_event(
            store, "correction_blocked",
            task_id=task_id,
            detail=f"pendency={pendency_id} reason={reason}",
        )
        return {
            "status": "blocked",
            "task_id": task_id,
            "pendency_id": pendency_id,
            "reason": reason,
        }

    log_event(
        store, "correction_allowed",
        task_id=task_id,
        detail=f"pendency={pendency_id} attempt={attempt_number}",
    )
    return {
        "status": "allowed",
        "task_id": task_id,
        "pendency_id": pendency_id,
        "attempt_number": attempt_number,
        "reason": reason,
    }


def check_scope_compliance(
    proposed_files: list[str],
    authorized_scope: list[str],
) -> tuple[bool, list[str]]:
    """Check if proposed changes are within authorized scope.

    Returns (compliant, out_of_scope_files).
    """
    import fnmatch

    if not authorized_scope:
        return True, []

    out_of_scope: list[str] = []
    for f in proposed_files:
        if not any(fnmatch.fnmatch(f, p) for p in authorized_scope):
            out_of_scope.append(f)

    return len(out_of_scope) == 0, out_of_scope
