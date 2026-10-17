
STATUS: RASCUNHO
date: 2026-09-01
decision-makers: ["Project owner"]
consulted: []
informed: ["Claude Code", "Codex"]

---

# Adopt MADR 4.0.0 with executable architecture fitness functions

## Context and Problem Statement

The repository is developed with human-governed software agents such as Claude Code and Codex. Architectural decisions must persist independently of conversation history and must not be duplicated inside agent-specific instruction files. How should architectural decisions be recorded, discovered by agents, and objectively confirmed during future implementation?

## Decision Drivers

- Maintain one canonical, version-controlled source for architecture decisions.
- Preserve decision context, alternatives, rationale, consequences, and confirmation criteria.
- Allow both humans and heterogeneous coding agents to consume the same architecture record.
- Avoid coupling architectural governance to paid model APIs or one agent vendor.
- Turn machine-checkable architectural constraints into deterministic PASS/FAIL checks.
- Preserve human authority over architectural acceptance and supersession.

## Considered Options

- Ad hoc architecture notes in agent instruction files.
- Nygard-style ADRs without a repository enforcement layer.
- MADR 4.0.0 records without executable confirmation.
- MADR 4.0.0 plus Docs-as-Code, architecture fitness functions, agent routing, and human governance.

## Decision Outcome

Chosen option: "MADR 4.0.0 plus Docs-as-Code, architecture fitness functions, agent routing, and human governance", because it separates decision authority, agent discovery, and deterministic enforcement while remaining repository-native and vendor-independent.

### Consequences

- Good, because architectural rationale remains in a durable Git-tracked record.
- Good, because Claude Code and Codex can follow the same decisions without duplicating them in vendor-specific files.
- Good, because machine-checkable constraints can fail closed in local validation and CI.
- Good, because the baseline does not require a paid LLM API or per-token billing.
- Bad, because architecture-significant changes require explicit decision maintenance and confirmation work.
- Bad, because fitness functions only enforce constraints that have actually been encoded; semantic review remains necessary for non-machine-checkable concerns.

### Confirmation

Automated:

- `FF-ADR-001` validates the ADR repository contract.
- `FF-GOV-001` runs governance regression tests.
- CI executes `python3 scripts/architecture/run_fitness_functions.py` for every pull request and protected-branch update.

Manual:

- Confirm that `CLAUDE.md` and `AGENTS.md` remain routing-only and do not become duplicate architecture sources.
- Confirm that new project-specific architectural invariants are linked to automated fitness functions whenever deterministic checking is feasible.

## Pros and Cons of the Options

### Ad hoc architecture notes in agent instruction files

- Good, because agents discover instructions quickly.
- Bad, because decisions are duplicated across agent-specific files.
- Bad, because rationale, alternatives, lifecycle, and confirmation are weak or absent.
- Bad, because multi-agent consistency becomes difficult to audit.

### Nygard-style ADRs without a repository enforcement layer

- Good, because the ADR format is simple and well established.
- Good, because decisions can be version-controlled.
- Bad, because the record alone does not deterministically detect architectural erosion.

### MADR 4.0.0 records without executable confirmation

- Good, because MADR captures drivers, options, outcome, consequences, and confirmation intent.
- Bad, because non-executed confirmation can remain aspirational and allow architecture drift.

### MADR 4.0.0 plus Docs-as-Code, architecture fitness functions, agent routing, and human governance

- Good, because decision, discovery, enforcement, and authority are explicitly separated.
- Good, because the same repository contract works with Claude Code, Codex, CI, and human review.
- Neutral, because some architectural qualities still require manual judgment.
- Bad, because the enforcement suite must evolve with the architecture.

## More Information

MADR is pinned to version 4.0.0. The upstream project publishes the MADR template and documents `Confirmation` as the place to describe automated or manual fitness functions. Source and licensing information are recorded in `THIRD_PARTY_NOTICES.md`.
