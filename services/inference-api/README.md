# Inference API

Thin FastAPI HTTP edge over `aarogya_core`. No OCR/training logic here.

```bash
# from repo root after bootstrap
make api
# or
uvicorn app.main:app --reload --port 8000
```

Health: `GET /api/v1/health`
Version: `GET /api/v1/version`
