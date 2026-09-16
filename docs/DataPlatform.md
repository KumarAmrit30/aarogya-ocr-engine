# Data Platform

The Research Data Platform (RDP) lives in `datasets/aarogya_datasets/` (package `aarogya-datasets`).

## Goals

- Dataset-agnostic ingest via `DatasetPipeline`
- Catalog in `datasets/registry.yaml` (IDs + pointers only)
- Immutable published versions under `datasets/versions/`
- Evaluation consumes **only** `DatasetManifest` / `DatasetSample` (+ fingerprint)

## Out of scope (Phase 3)

Downloads, OCR, real converters, cloud object stores, redaction UIs, training.

## Quick start

```bash
pip install -e "./datasets[dev]"
python -c "from aarogya_datasets.pipeline import DefaultDatasetPipeline"
```

Synthetic demo:

```python
from pathlib import Path
from aarogya_core.types.data_platform import DatasetSource
from aarogya_datasets.pipeline import DefaultDatasetPipeline

DefaultDatasetPipeline(Path(".")).run(
    DatasetSource(name="synthetic", kind="synthetic"),
    {"dataset_id": "DATASET-00001", "version": "v1", "name": "demo"},
)
```

Or `POST /api/v1/datasets/pipeline/run`.

## Layout

See `DatasetArchitecture.md`, `DatasetPipeline.md`, `DatasetRegistry.md`.
