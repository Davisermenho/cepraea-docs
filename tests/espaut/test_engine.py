#!/usr/bin/env python3
"""Execute predeclared tests for the state machine engine."""

from __future__ import annotations

import enum
import json
import sys
from pathlib import Path
from typing import Any

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.engine import StateMachine, TransitionError


PLAN_PATH = Path(__file__).with_name("test_cases_engine.json")


class St(enum.StrEnum):
    A = "A"
    B = "B"
    C = "C"


TRANSITIONS = {
    (St.A, "go"): St.B,
    (St.A, "guarded_go"): St.B,
    (St.B, "advance"): St.C,
}


def _allow_guard(state: enum.StrEnum, event: str, ctx: dict[str, Any]) -> bool:
    return ctx.get("allow", False)


GUARDS = {(St.A, "guarded_go"): _allow_guard}


def load_plan() -> dict[str, Any]:
    return json.loads(PLAN_PATH.read_text(encoding="utf-8"))


def case(plan: dict[str, Any], test_id: str) -> dict[str, Any]:
    return next(item for item in plan["tests"] if item["id"] == test_id)


def run_tests() -> list[dict[str, Any]]:
    plan = load_plan()
    results: list[dict[str, Any]] = []

    for spec in plan["tests"]:
        tid = spec["id"]
        title = spec["title"]
        result = {"id": tid, "title": title, "status": "FAIL", "detail": ""}

        try:
            check = spec.get("check")

            if check == "valid_events":
                sm = StateMachine("test", TRANSITIONS)
                state = St(spec["initial_state"])
                actual = sorted(sm.valid_events(state))
                expected = sorted(spec["expected_events"])
                if actual == expected:
                    result["status"] = "PASS"
                else:
                    result["detail"] = f"expected={expected} actual={actual}"

            elif check == "can_transition":
                sm = StateMachine("test", TRANSITIONS, GUARDS)
                state = St(spec["initial_state"])
                ctx = spec.get("context", {})
                actual = sm.can_transition(state, spec["event"], ctx)
                if actual == spec["expected"]:
                    result["status"] = "PASS"
                else:
                    result["detail"] = f"expected={spec['expected']} actual={actual}"

            elif check == "callback_invoked":
                invocations: list[tuple[str, ...]] = []

                def cb(
                    name: str,
                    old: enum.StrEnum,
                    ev: str,
                    new: enum.StrEnum,
                    ctx: dict[str, Any],
                ) -> None:
                    invocations.append((name, old.value, ev, new.value))

                sm = StateMachine("test", TRANSITIONS, on_transition=cb)
                state = St(spec["initial_state"])
                sm.transition(state, spec["event"])
                if len(invocations) == 1 and invocations[0] == ("test", "A", "go", "B"):
                    result["status"] = "PASS"
                else:
                    result["detail"] = f"invocations={invocations}"

            elif "events" in spec:
                sm = StateMachine("test", TRANSITIONS, GUARDS)
                state = St(spec["initial_state"])
                for ev in spec["events"]:
                    state = sm.transition(state, ev)
                if state.value == spec["expected_state"]:
                    result["status"] = "PASS"
                else:
                    result["detail"] = f"expected={spec['expected_state']} actual={state.value}"

            else:
                sm = StateMachine("test", TRANSITIONS, GUARDS)
                state = St(spec["initial_state"])
                ctx = spec.get("context", {})
                try:
                    new_state = sm.transition(state, spec["event"], ctx)
                    if spec["expected_error"]:
                        result["detail"] = f"expected error, got state={new_state.value}"
                    elif new_state.value == spec["expected_state"]:
                        result["status"] = "PASS"
                    else:
                        result["detail"] = f"expected={spec['expected_state']} actual={new_state.value}"
                except TransitionError:
                    if spec["expected_error"]:
                        result["status"] = "PASS"
                    else:
                        result["detail"] = "unexpected TransitionError"

        except Exception as exc:
            result["detail"] = f"exception: {exc}"

        results.append(result)

    return results


def main() -> int:
    results = run_tests()
    passed = sum(1 for r in results if r["status"] == "PASS")
    total = len(results)

    for r in results:
        mark = "PASS" if r["status"] == "PASS" else "FAIL"
        line = f"  [{mark}] {r['id']} — {r['title']}"
        if r["detail"]:
            line += f"  ({r['detail']})"
        print(line)

    print(f"\nengine: {passed}/{total} passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
