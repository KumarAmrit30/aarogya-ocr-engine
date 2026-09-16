# Engines

An engine is a **system** (detector + recognizer + layout + …), not a single checkpoint.

## Layout

```text
engines/<name>/
  detector.py
  recognizer.py
  layout.py
  table.py
  reading_order.py
  pipeline.py      # build_pipeline(config) -> BasePipeline
  README.md
```

## Adding an engine

1. Copy `engines/_template/` → `engines/<name>/`.
2. Implement adapters against `aarogya_core.interfaces`.
3. Register a pipeline factory via `aarogya_core.pipeline.compose.register_pipeline_factory`.
4. Add config under `configs/engines/<name>.yaml`.
5. Document future Python deps in the engine README — install them only when implementing.

## Rule

Engines never define competing `OCRResult` / `Metrics` types.
