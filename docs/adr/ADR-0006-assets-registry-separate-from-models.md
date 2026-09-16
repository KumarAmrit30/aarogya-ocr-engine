# ADR-0006: Assets registry separate from models

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

Checkpoints, ONNX/TensorRT exports, tokenizers, vocabs, lexicons, prompts, and templates accumulate quickly. Treating them as “models” conflates logical identity with files on disk.

## Decision

Introduce `assets/` with `ASSET-#####` catalog. `MODEL-#####` remains the logical model; assets are consumable files referenced by models/pipelines.

## Consequences

- Large binaries stay gitignored under `assets/*/`.
- Pipelines may list `asset_ids`.
- Export formats can evolve without new model IDs.

## Alternatives considered

- Store everything under `registry/models/` — rejected (overloads meaning).
- Only filesystem paths in configs — rejected (no stable IDs for lineage).
