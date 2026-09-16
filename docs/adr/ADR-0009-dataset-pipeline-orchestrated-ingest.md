# ADR-0009: Dataset ingest is pipeline-orchestrated

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

Ad-hoc scripts per dataset do not scale and diverge from the OCR `Pipeline` pattern used elsewhere in the Research Platform.

## Decision

All ingest goes through `DatasetPipeline.run(source, config) → PublishedVersionResult` with pluggable steps (load → convert → validate → stats → quality → card → fingerprint → lineage → immutable write → registry → events).

## Consequences

- Phase 4 becomes `pipeline.run(...)` with one real converter
- Dataset names are not hardcoded in the orchestrator
- Events enable future loose coupling (stats→quality→card subscribers)

## Alternatives considered

- One-off CLI scripts per dataset — rejected for Phase 3+
- Hardcoded mega-function — rejected (not extensible)
