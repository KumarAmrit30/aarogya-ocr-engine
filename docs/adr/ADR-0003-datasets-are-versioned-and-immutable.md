# ADR-0003: Datasets are versioned (and scientifically immutable)

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

A dataset name like “RxHandBD” changes meaning as labels are cleaned, splits change, or augmentations are added. Comparing models across silent mutations invalidates science.

## Decision

Identity is `Dataset (DATASET-#####) → Version (v1, v2, …) → Split`. Evaluation and benchmarks always cite **dataset_id + dataset_version**. Published versions are not rewritten; create `vN+1` instead.

## Consequences

- Registry schema includes nested `versions`.
- Reports say e.g. `DATASET-00007@v3`, not just a name.
- Historical results remain interpretable years later.

## Alternatives considered

- Single mutable dataset folder — rejected (silent invalidation).
- Git-only versioning without IDs — rejected (harder for registries/UI).
