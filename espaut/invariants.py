#!/usr/bin/env python3
"""INV-001 through INV-014 as callable predicates."""

from __future__ import annotations

from typing import Any

from espaut.security import contains_secret


def inv_001_identity(task: dict[str, Any], other_tasks: list[dict[str, Any]]) -> tuple[bool, str]:
    """INV-001: Do not confuse tasks by similar branch/title names."""
    branch = task.get("branch_name")
    if not branch:
        return True, "no branch assigned"
    conflicts = [t for t in other_tasks if t["task_id"] != task["task_id"] and t.get("branch_name") == branch]
    if conflicts:
        ids = [t["task_id"] for t in conflicts]
        return False, f"branch {branch} shared with tasks: {ids}"
    return True, "unique branch"


def inv_002_preservation(changes_eligible: list[str], changes_committed: list[str]) -> tuple[bool, str]:
    """INV-002: Do not discard preexisting modifications without authorization."""
    uncommitted = set(changes_eligible) - set(changes_committed)
    if uncommitted:
        return False, f"uncommitted eligible files: {sorted(uncommitted)}"
    return True, "all eligible changes committed"


def inv_003_traceability(task: dict[str, Any]) -> tuple[bool, str]:
    """INV-003: Changes attributed to the task have a verifiable link."""
    commits = task.get("commit_shas", [])
    if not commits:
        return False, "no commits linked to task"
    return True, f"{len(commits)} commits linked"


def inv_004_revision_validity(
    check_revision: str | None,
    current_revision: str | None,
) -> tuple[bool, str]:
    """INV-004: Check is only valid for the revision it corresponds to."""
    if not check_revision or not current_revision:
        return False, "revision information missing"
    if check_revision != current_revision:
        return False, f"check revision {check_revision[:8]} != current {current_revision[:8]}"
    return True, "revision matches"


def inv_005_evidence(claim: str, evidence: dict[str, Any] | None) -> tuple[bool, str]:
    """INV-005: AI declaration does not suffice to prove execution or success."""
    if evidence is None:
        return False, f"no evidence for: {claim}"
    if evidence.get("source_system") == "ai_inference":
        return False, "AI inference alone is not evidence"
    return True, f"evidence from {evidence.get('source_system', '?')}"


def inv_006_pendencies(pendencies: list[dict[str, Any]]) -> tuple[bool, str]:
    """INV-006: Blocking applicable pendency cannot be omitted from closure."""
    blocking = [
        p for p in pendencies
        if p.get("blocking_effect")
        and p.get("resolution_state") not in ("RESOLVIDA", "JUSTIFICADA")
    ]
    if blocking:
        ids = [p["pendency_id"] for p in blocking]
        return False, f"unresolved blocking pendencies: {ids}"
    return True, "no unresolved blocking pendencies"


def inv_007_conversations(threads: list[dict[str, Any]]) -> tuple[bool, str]:
    """INV-007: Code update does not automatically resolve a conversation."""
    unresolved = [t for t in threads if not t.get("is_resolved") and not t.get("is_outdated")]
    if unresolved:
        return False, f"{len(unresolved)} unresolved conversation(s)"
    return True, "all conversations resolved or outdated"


def inv_008_authority(
    operation: str,
    required_permission: str,
    granted_permissions: set[str],
) -> tuple[bool, str]:
    """INV-008: Decisions reserved to the user require authorization."""
    if required_permission not in granted_permissions:
        return False, f"operation {operation!r} requires permission {required_permission!r}"
    return True, f"permission {required_permission!r} granted"


def inv_009_idempotency(
    operation_id: str,
    completed_operations: set[str],
) -> tuple[bool, str]:
    """INV-009: Resumption must not duplicate undue effects."""
    if operation_id in completed_operations:
        return False, f"operation {operation_id} already completed"
    return True, "operation not yet completed"


def inv_010_recoverability(operation: dict[str, Any]) -> tuple[bool, str]:
    """INV-010: Persistent operations leave recoverable references."""
    ref = operation.get("reference") or operation.get("sha") or operation.get("evidence_id")
    if not ref:
        return False, "no recoverable reference for operation"
    return True, f"reference: {ref}"


def inv_011_secrets(content: str) -> tuple[bool, str]:
    """INV-011: Do not deliberately forward identified secrets."""
    findings = contains_secret(content)
    if findings:
        return False, f"secret detected: {findings[0]}"
    return True, "no secrets detected"


def inv_012_closure(
    subtests_passed: bool,
    checks_passed: bool,
    criteria_met: bool,
) -> tuple[bool, str]:
    """INV-012: Subtest/check/commit success alone does not approve the task."""
    if not criteria_met:
        reasons = []
        if subtests_passed:
            reasons.append("subtests pass but criteria not met")
        if checks_passed:
            reasons.append("checks pass but criteria not met")
        return False, "; ".join(reasons) if reasons else "criteria not met"
    return True, "all criteria met"


def inv_013_currency(
    evaluated_revision: str | None,
    current_revision: str | None,
) -> tuple[bool, str]:
    """INV-013: Revision change invalidates conclusions from the prior revision."""
    if not evaluated_revision or not current_revision:
        return False, "revision information incomplete"
    if evaluated_revision != current_revision:
        return False, f"stale: evaluated {evaluated_revision[:8]} != current {current_revision[:8]}"
    return True, "conclusions current"


def inv_014_fidelity(record: dict[str, Any]) -> tuple[bool, str]:
    """INV-014: Internal representations preserve reference to the original source."""
    source = record.get("source_reference") or record.get("origin_reference")
    if not source:
        return False, "no source reference preserved"
    return True, f"source: {source}"
