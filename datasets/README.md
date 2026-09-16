# Research Data Platform

Single source of truth for every dataset. Package: `aarogya_datasets`.

```bash
pip install -e "./datasets[dev]"
```

Orchestrator: `aarogya_datasets.pipeline.DefaultDatasetPipeline`.

Evaluation consumes **only** `DatasetManifest` / `DatasetSample` — never loaders/validators.

See `docs/DataPlatform.md`.
