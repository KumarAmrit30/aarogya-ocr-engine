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

Domain types: `aarogya_core.types`. Metrics: `aarogya_evaluation`.
