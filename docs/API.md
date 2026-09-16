# API

Base path: `/api/v1`  
OpenAPI: `http://localhost:8000/docs`  
Schema version: `1.0`

| Method | Path | Status |
|--------|------|--------|
| GET | `/health` | Working |
| GET | `/version` | Working |
| POST | `/ocr` | Placeholder (`not_implemented` via StubOCRPipeline) |
| POST | `/train` | Placeholder |
| POST | `/evaluate` | **Working** — EvaluationEngine on GT/prediction pairs |
| GET | `/evaluation/reports` | Working — lists saved JSON reports |
| GET | `/benchmarks` | Working — lists suite folders |
| GET | `/models` | Placeholder empty list |
| GET | `/datasets` | Working — catalog + search filters |
| GET | `/datasets/{id}` | Working |
| GET | `/datasets/{id}/versions/{version}` | Working — fingerprint, validation, quality, lineage, card |
| GET | `/datasets/{id}/preview` | Working — sample metadata preview |
| POST | `/datasets/pipeline/run` | Working — synthetic DefaultDatasetPipeline (no downloads) |

Domain types: `aarogya_core.types`. Metrics: `aarogya_evaluation`. Datasets: `aarogya_datasets`.
