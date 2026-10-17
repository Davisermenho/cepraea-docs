#!/usr/bin/env python3
"""CI/check monitoring — Check state machine (SM #3, CTX-04)."""

from __future__ import annotations

import enum
from pathlib import Path
from typing import Any

from espaut.engine import StateMachine
from espaut.events import log_event
from espaut.gh_ops import pr_checks_json
from espaut.store import load_config, write_json


class CheckState(enum.StrEnum):
    NAO_CONFIGURADO = "NAO_CONFIGURADO"
    NAO_OBSERVADO = "NAO_OBSERVADO"
    PENDENTE = "PENDENTE"
    APROVADO = "APROVADO"
    REPROVADO = "REPROVADO"
    CANCELADO = "CANCELADO"
    IGNORADO = "IGNORADO"
    INDETERMINADO = "INDETERMINADO"


GH_STATE_MAP: dict[tuple[str, str], CheckState] = {
    ("SUCCESS", ""): CheckState.APROVADO,
    ("", "success"): CheckState.APROVADO,
    ("", "SUCCESS"): CheckState.APROVADO,
    ("FAILURE", ""): CheckState.REPROVADO,
    ("", "failure"): CheckState.REPROVADO,
    ("", "FAILURE"): CheckState.REPROVADO,
    ("PENDING", ""): CheckState.PENDENTE,
    ("", "pending"): CheckState.PENDENTE,
    ("", "PENDING"): CheckState.PENDENTE,
    ("CANCELLED", ""): CheckState.CANCELADO,
    ("", "cancelled"): CheckState.CANCELADO,
    ("", "CANCELLED"): CheckState.CANCELADO,
    ("NEUTRAL", ""): CheckState.APROVADO,
    ("", "neutral"): CheckState.APROVADO,
    ("SKIPPED", ""): CheckState.IGNORADO,
    ("", "skipped"): CheckState.IGNORADO,
    ("STALE", ""): CheckState.INDETERMINADO,
    ("", "stale"): CheckState.INDETERMINADO,
    ("STARTUP_FAILURE", ""): CheckState.REPROVADO,
    ("", "startup_failure"): CheckState.REPROVADO,
    ("ACTION_REQUIRED", ""): CheckState.PENDENTE,
    ("", "action_required"): CheckState.PENDENTE,
    ("TIMED_OUT", ""): CheckState.REPROVADO,
    ("", "timed_out"): CheckState.REPROVADO,
}


def normalize_check_state(raw: dict[str, Any]) -> CheckState:
    """Map a raw gh check/status record to a normalized CheckState."""
    state = raw.get("state", "")
    conclusion = raw.get("conclusion", "")
    key = (state, conclusion)
    if key in GH_STATE_MAP:
        return GH_STATE_MAP[key]
    for k, v in GH_STATE_MAP.items():
        if k[0] and k[0].lower() == state.lower():
            return v
        if k[1] and k[1].lower() == conclusion.lower():
            return v
    return CheckState.INDETERMINADO


def make_check_record(
    raw: dict[str, Any],
    *,
    pr_number: int,
    evaluated_revision: str | None = None,
) -> dict[str, Any]:
    """Build a normalized check record from raw gh data."""
    normalized = normalize_check_state(raw)
    return {
        "name": raw.get("name", "unknown"),
        "pr_number": pr_number,
        "evaluated_revision": evaluated_revision,
        "raw_state": raw.get("state", ""),
        "raw_conclusion": raw.get("conclusion", ""),
        "normalized_result": normalized.value,
        "execution_url": raw.get("detailsUrl", ""),
        "started_at": raw.get("startedAt"),
        "completed_at": raw.get("completedAt"),
    }


def query_checks(
    store: Path,
    task_id: str,
    pr_number: int,
    evaluated_revision: str | None = None,
    cwd: str | None = None,
) -> dict[str, Any]:
    """Query checks for a PR and return a normalized report."""
    raw_checks = pr_checks_json(pr_number, cwd=cwd)

    if not raw_checks:
        config = load_config(store)
        if config.get("ci_required", False):
            log_event(
                store, "checks_not_configured",
                task_id=task_id,
                object_reference=str(pr_number),
            )
            return {
                "status": "not_configured",
                "task_id": task_id,
                "pr_number": pr_number,
                "checks": [],
                "aggregate": CheckState.NAO_CONFIGURADO.value,
            }
        return {
            "status": "not_configured",
            "task_id": task_id,
            "pr_number": pr_number,
            "checks": [],
            "aggregate": CheckState.NAO_CONFIGURADO.value,
        }

    records = [
        make_check_record(c, pr_number=pr_number, evaluated_revision=evaluated_revision)
        for c in raw_checks
    ]

    aggregate = compute_aggregate(records)

    log_event(
        store, "checks_queried",
        task_id=task_id,
        object_reference=str(pr_number),
        detail=f"total={len(records)} aggregate={aggregate.value}",
    )

    cache_path = store / "cache" / f"checks-PR{pr_number}.json"
    write_json(cache_path, {
        "pr_number": pr_number,
        "evaluated_revision": evaluated_revision,
        "checks": records,
        "aggregate": aggregate.value,
    })

    return {
        "status": "queried",
        "task_id": task_id,
        "pr_number": pr_number,
        "checks": records,
        "aggregate": aggregate.value,
    }


def compute_aggregate(checks: list[dict[str, Any]]) -> CheckState:
    """Compute aggregate check state from individual results."""
    if not checks:
        return CheckState.NAO_CONFIGURADO

    states = {CheckState(c["normalized_result"]) for c in checks}

    if CheckState.REPROVADO in states:
        return CheckState.REPROVADO
    if CheckState.PENDENTE in states:
        return CheckState.PENDENTE
    if CheckState.CANCELADO in states:
        return CheckState.CANCELADO
    if CheckState.INDETERMINADO in states:
        return CheckState.INDETERMINADO
    if all(s in (CheckState.APROVADO, CheckState.IGNORADO) for s in states):
        return CheckState.APROVADO
    return CheckState.INDETERMINADO
