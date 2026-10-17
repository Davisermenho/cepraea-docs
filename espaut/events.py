#!/usr/bin/env python3
"""Append-only event log and evidence creation for ESP-AUT-GIT-001."""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
from typing import Any

from espaut.store import append_jsonl, new_id, write_json


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def make_event(
    event_type: str,
    *,
    task_id: str | None = None,
    execution_id: str | None = None,
    actor: str = "espaut",
    object_reference: str | None = None,
    old_state: str | None = None,
    new_state: str | None = None,
    outcome: str | None = None,
    evidence_id: str | None = None,
    detail: str | None = None,
) -> dict[str, Any]:
    """Build an event record without persisting it."""
    record: dict[str, Any] = {
        "event_id": new_id("EVT-"),
        "event_type": event_type,
        "occurred_at": _now_iso(),
        "actor": actor,
    }
    if task_id is not None:
        record["task_id"] = task_id
    if execution_id is not None:
        record["execution_id"] = execution_id
    if object_reference is not None:
        record["object_reference"] = object_reference
    if old_state is not None:
        record["old_state"] = old_state
    if new_state is not None:
        record["new_state"] = new_state
    if outcome is not None:
        record["outcome"] = outcome
    if evidence_id is not None:
        record["evidence_id"] = evidence_id
    if detail is not None:
        record["detail"] = detail
    return record


def emit_event(store: Path, event: dict[str, Any]) -> None:
    """Append an event to the store's event log."""
    append_jsonl(store / "events.jsonl", event)


def log_event(
    store: Path,
    event_type: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Create and persist an event in one call. Returns the event record."""
    event = make_event(event_type, **kwargs)
    emit_event(store, event)
    return event


def make_evidence(
    source_system: str,
    source_reference: str,
    observation: str,
    *,
    task_id: str | None = None,
    related_revision: str | None = None,
) -> dict[str, Any]:
    """Build an evidence record with integrity hash."""
    evidence_id = new_id("EVD-")
    record: dict[str, Any] = {
        "evidence_id": evidence_id,
        "source_system": source_system,
        "source_reference": source_reference,
        "observed_at": _now_iso(),
        "observation": observation,
    }
    if task_id is not None:
        record["task_id"] = task_id
    if related_revision is not None:
        record["related_revision"] = related_revision
    canonical = json.dumps(record, ensure_ascii=False, sort_keys=True)
    record["integrity_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return record


def save_evidence(store: Path, evidence: dict[str, Any]) -> Path:
    """Persist an evidence record and return its file path."""
    eid = evidence["evidence_id"]
    path = store / "evidence" / f"{eid}.json"
    write_json(path, evidence)
    return path
