# ADR-0007: Evaluation stays independent of the Data Platform

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

The Research Data Platform introduces loaders, validators, quality, cards, and `DatasetPipeline`. Evaluation must remain model-agnostic and reusable without coupling to ingest internals.

## Decision

Evaluation and benchmarks may consume only `DatasetManifest`, `DatasetSample`, and fingerprints (from `aarogya_core.types` or thin `aarogya_datasets.exports`). They **must not** import loaders, validators, quality, cards, or pipeline modules.

## Consequences

- Clear packaging boundary; eval stays lightweight
- Optional export helpers materialize manifests without leaking internals
- Phase 4+ loaders never force eval refactors

## Alternatives considered

- Evaluation owning loaders — rejected (duplicates RDP, couples concerns)
- Shared “kitchen sink” data package — rejected (hard to evolve independently)
