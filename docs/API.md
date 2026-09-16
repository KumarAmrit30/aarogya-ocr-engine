# API

Base path: `/api/v1`  
OpenAPI: `http://localhost:8000/docs`  
Schema version: `1.0` (`api_schema_version`)

| Method | Path | Status |
|--------|------|--------|
| GET | `/health` | Working |
| GET | `/version` | Working |
| POST | `/ocr` | Placeholder — returns `OCRResult` with `status=not_implemented` via `StubOCRPipeline` |
| POST | `/train` | Placeholder |
| POST | `/evaluate` | Placeholder |
| GET | `/models` | Placeholder empty list |

Domain types live in `aarogya_core.types`. HTTP DTOs in `services/inference-api/app/schemas`. TypeScript mirrors in `@aarogya/shared`.

CORS origins from `CORS_ORIGINS`. Request tracing via `X-Request-ID`.
