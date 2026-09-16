# ADR-0004: Experiments are immutable

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

Editing `EXP-0015` after the fact destroys auditability. Real labs freeze runs.

## Decision

Never mutate an allocated `EXP-#####`. Layout is frozen (`config/`, `results/`, `report/`, `artifacts/`). A rerun allocates a **new** ID (optionally `supersedes` the previous).

## Consequences

- Writers raise if the experiment directory already exists.
- Artifact paths remain stable forever.
- Comparison across experiments is trustworthy.

## Alternatives considered

- Overwrite in place with timestamps — rejected (lossy).
- Mutable “latest” symlink only — allowed as a convenience pointer, never as the source of truth.
