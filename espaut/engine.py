#!/usr/bin/env python3
"""Generic state machine engine serving all ESP-AUT-GIT-001 state machines."""

from __future__ import annotations

import enum
from typing import Any, Callable


class TransitionError(Exception):
    """Raised when a transition is invalid or blocked by a guard."""


Guard = Callable[[enum.StrEnum, str, dict[str, Any]], bool]

TransitionTable = dict[tuple[enum.StrEnum, str], enum.StrEnum]


class StateMachine:
    """Reusable state machine driven by a transition table.

    Parameters
    ----------
    name:
        Human-readable name for logging/events (e.g. "task", "pendency").
    transitions:
        Mapping of ``(current_state, event_name) -> target_state``.
    guards:
        Optional mapping of ``(current_state, event_name) -> predicate``.
        The predicate receives ``(current_state, event, context)`` and must
        return ``True`` to allow the transition.
    on_transition:
        Optional callback invoked after every successful transition with
        ``(name, old_state, event, new_state, context)``.
    """

    def __init__(
        self,
        name: str,
        transitions: TransitionTable,
        guards: dict[tuple[enum.StrEnum, str], Guard] | None = None,
        on_transition: Callable[
            [str, enum.StrEnum, str, enum.StrEnum, dict[str, Any]], None
        ]
        | None = None,
    ) -> None:
        self.name = name
        self._transitions = dict(transitions)
        self._guards: dict[tuple[enum.StrEnum, str], Guard] = dict(guards or {})
        self._on_transition = on_transition

    @property
    def transitions(self) -> TransitionTable:
        return dict(self._transitions)

    def valid_events(self, state: enum.StrEnum) -> list[str]:
        """Return the event names available from *state*."""
        return [ev for (s, ev) in self._transitions if s == state]

    def can_transition(
        self,
        state: enum.StrEnum,
        event: str,
        context: dict[str, Any] | None = None,
    ) -> bool:
        """Return whether *event* is allowed from *state* without applying it."""
        key = (state, event)
        if key not in self._transitions:
            return False
        guard = self._guards.get(key)
        if guard is not None and not guard(state, event, context or {}):
            return False
        return True

    def transition(
        self,
        state: enum.StrEnum,
        event: str,
        context: dict[str, Any] | None = None,
    ) -> enum.StrEnum:
        """Apply *event* to *state* and return the new state.

        Raises ``TransitionError`` when the transition is undefined or
        when a guard rejects it.
        """
        ctx = context or {}
        key = (state, event)
        target = self._transitions.get(key)
        if target is None:
            valid = self.valid_events(state)
            raise TransitionError(
                f"[{self.name}] no transition for event {event!r} "
                f"from state {state.value!r}; valid events: {valid}"
            )
        guard = self._guards.get(key)
        if guard is not None and not guard(state, event, ctx):
            raise TransitionError(
                f"[{self.name}] guard blocked transition "
                f"{state.value!r} --[{event}]--> {target.value!r}"
            )
        if self._on_transition is not None:
            self._on_transition(self.name, state, event, target, ctx)
        return target
