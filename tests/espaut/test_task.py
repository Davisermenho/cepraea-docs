#!/usr/bin/env python3
"""Tests for task entity and state machine."""

from __future__ import annotations

import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.engine import TransitionError
from espaut.task import TaskState, build_task_machine, make_task


def test_make_task() -> dict[str, str]:
    t = make_task("TASK-001", "/repo", "Test task", objective="do stuff")
    return {
        "task_id": "PASS" if t["task_id"] == "TASK-001" else "FAIL",
        "initial_state": "PASS" if t["state"] == "REGISTRADA" else "FAIL",
        "has_created_at": "PASS" if t["created_at"] else "FAIL",
        "branch_none": "PASS" if t["branch_name"] is None else "FAIL",
    }


def test_happy_path() -> dict[str, str]:
    sm = build_task_machine()
    state = TaskState.REGISTRADA
    state = sm.transition(state, "prepare")
    c1 = state == TaskState.PREPARADA
    state = sm.transition(state, "start")
    c2 = state == TaskState.EM_EXECUCAO
    state = sm.transition(state, "changes_detected")
    c3 = state == TaskState.PRESERVACAO_PENDENTE
    state = sm.transition(state, "submit_review")
    c4 = state == TaskState.EM_REVISAO
    state = sm.transition(state, "await_decision")
    c5 = state == TaskState.AGUARDANDO_DECISAO
    state = sm.transition(state, "approve_integration")
    c6 = state == TaskState.APTA_PARA_INTEGRACAO
    state = sm.transition(state, "merge_confirmed")
    c7 = state == TaskState.INTEGRADA
    return {
        "prepare": "PASS" if c1 else "FAIL",
        "start": "PASS" if c2 else "FAIL",
        "changes": "PASS" if c3 else "FAIL",
        "review": "PASS" if c4 else "FAIL",
        "decision": "PASS" if c5 else "FAIL",
        "approve": "PASS" if c6 else "FAIL",
        "integrated": "PASS" if c7 else "FAIL",
    }


def test_correction_cycle() -> dict[str, str]:
    sm = build_task_machine()
    state = TaskState.EM_REVISAO
    state = sm.transition(state, "request_correction")
    c1 = state == TaskState.EM_CORRECAO
    state = sm.transition(state, "correction_applied")
    c2 = state == TaskState.EM_REVISAO
    return {
        "to_correction": "PASS" if c1 else "FAIL",
        "back_to_review": "PASS" if c2 else "FAIL",
    }


def test_block_and_unblock() -> dict[str, str]:
    sm = build_task_machine()
    state = TaskState.EM_EXECUCAO
    state = sm.transition(state, "block")
    c1 = state == TaskState.BLOQUEADA
    state = sm.transition(state, "unblock")
    c2 = state == TaskState.EM_EXECUCAO
    return {
        "blocked": "PASS" if c1 else "FAIL",
        "unblocked": "PASS" if c2 else "FAIL",
    }


def test_interrupt_and_resume() -> dict[str, str]:
    sm = build_task_machine()
    state = TaskState.EM_EXECUCAO
    state = sm.transition(state, "interrupt")
    c1 = state == TaskState.INTERROMPIDA
    state = sm.transition(state, "resume")
    c2 = state == TaskState.EM_EXECUCAO
    return {
        "interrupted": "PASS" if c1 else "FAIL",
        "resumed": "PASS" if c2 else "FAIL",
    }


def test_invalid_transition() -> dict[str, str]:
    sm = build_task_machine()
    try:
        sm.transition(TaskState.INTEGRADA, "start")
        return {"rejects": "FAIL"}
    except TransitionError:
        return {"rejects": "PASS"}


def test_invalidation_from_apt() -> dict[str, str]:
    sm = build_task_machine()
    state = sm.transition(TaskState.APTA_PARA_INTEGRACAO, "invalidated")
    return {
        "back_to_review": "PASS" if state == TaskState.EM_REVISAO else "FAIL",
    }


ALL_TESTS = [
    ("make_task", test_make_task),
    ("happy_path", test_happy_path),
    ("correction_cycle", test_correction_cycle),
    ("block_and_unblock", test_block_and_unblock),
    ("interrupt_and_resume", test_interrupt_and_resume),
    ("invalid_transition", test_invalid_transition),
    ("invalidation_from_apt", test_invalidation_from_apt),
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

    print(f"\ntask: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
