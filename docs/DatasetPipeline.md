# Dataset Pipeline

Executable ingest orchestrator (same idea as OCR `Pipeline`).

## Steps (`DefaultDatasetPipeline`)

1. Load (synthetic stub / plugins)
2. Convert (`IdentityConverter` today)
3. Validate (structural)
4. Statistics
5. Quality (skipped if validation failed unless `allow_failed_validation`)
6. Card
7. Fingerprint
8. Lineage edge append
9. Immutable version write via `LocalStorage`
10. Registry catalog update
11. Emit `Dataset*` events

## Config

See `configs/datasets/example_pipeline.yaml`.

```python
from aarogya_datasets.pipeline import compose_pipeline
pipe = compose_pipeline(repo_root, "default")
pipe.run(source, config)
```

## Events

In-process `EventBus`: `dataset_loaded`, `dataset_validated`, `statistics_generated`, `quality_computed`, `fingerprint_computed`, `manifest_written`, `card_generated`, `version_published`.
