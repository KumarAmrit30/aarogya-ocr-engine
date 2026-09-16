# ADR-0002: Pipelines are registry-driven

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

Production systems compose detectors, recognizers, reading-order, and medical parsers in different combinations. Benchmarking a single “model” misrepresents system quality.

## Decision

Register compositions as `PIPELINE-#####` under `registry/pipelines/`. **Benchmarks key on pipelines**, not bare engines.

## Consequences

- Leaderboards show `PIPELINE-#####` × `DATASET-#####@vN`.
- Pipelines reference opaque engine/component IDs and optional `ASSET-#####` files.
- Manual ad-hoc wiring is discouraged for reported results.

## Alternatives considered

- Benchmark only `engine_id` — rejected (hides composition effects).
- Hard-code pipelines in Python — rejected (not reviewable/versionable).
