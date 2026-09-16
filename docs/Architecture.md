# Architecture

## Principle: Research Core first

The API and UI are **edges**. They depend on the Research Core — not the other way around.

```text
Research Core
  core/  datasets/  training/  evaluation/  benchmarks/  registry/  configs/  engines/
        │
        ├─ FastAPI (services/inference-api)
        ├─ CLI runners (scripts/)
        └─ Next.js research UI (apps/web)  ← talks to API only

Sandboxes (must not be imported by production paths)
  lab/   research/
```

## Dependency rules

1. `engines/*` implement `core` interfaces; they never redefine `OCRResult` / `Metrics`.
2. `services/inference-api` imports `aarogya_core` and delegates to `Pipeline`.
3. `apps/web` talks HTTP only (`@aarogya/shared` types).
4. `lab/` may import core/engines; **nothing** in core/engines/CI imports `lab/`.

## Pipelines

Pipelines are the unit researchers swap and benchmark:

`preprocess → detect → recognize → reading_order → postprocess`

Foundation ships `StubOCRPipeline` with `status=not_implemented`.

## Engines vs models

PaddleOCR is an **engine system** (detector + recognizer + layout + …), not one model file. Same for Qwen, Florence, etc. Adapters live under `engines/<name>/`.

## Traceability

Structured logs carry `request_id`, `experiment_id`, `run_id`, `config_hash`, `engine_id`. Registry IDs: `EXP-#####`, `DATASET-#####`, `MODEL-#####`.
