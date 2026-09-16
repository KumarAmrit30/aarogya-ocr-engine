# Dataset Explorer

Web: `/datasets` (filters) and `/datasets/[id]` (version detail).

API:

- `GET /api/v1/datasets?language=&license=&task=&script=&domain=&min_quality=&tags=&pii_status=&name_contains=`
- `GET /api/v1/datasets/{id}`
- `GET /api/v1/datasets/{id}/versions/{version}`
- `GET /api/v1/datasets/{id}/preview`
- `POST /api/v1/datasets/pipeline/run` — synthetic demo (no downloads)

Search is an in-memory linear filter over the catalog (contract for 100+ datasets; no search engine yet).
