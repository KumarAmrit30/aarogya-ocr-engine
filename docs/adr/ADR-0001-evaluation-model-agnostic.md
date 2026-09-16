# ADR-0001: Evaluation is model-agnostic

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

The platform will host many OCR/HTR/VLM engines (Paddle, PARSeq, TrOCR, Qwen, Florence, Document AI, Gemini, …). Embedding engine knowledge into the evaluation module would force constant rewrites and prevent fair comparison.

## Decision

The evaluation engine understands only **GroundTruth → Prediction → Metrics → Reports**. It must not import or special-case any engine package.

## Consequences

- Engines emit `Prediction` objects (optionally tagged with opaque `pipeline_id` / `engine_id`).
- New engines require zero evaluation code changes.
- Metrics remain the single source of truth under `evaluation/`.

## Alternatives considered

- Engine-specific evaluators — rejected (duplication, unfair comparison).
- Shared “OCR service” that owns both inference and metrics — rejected (couples research layers).
