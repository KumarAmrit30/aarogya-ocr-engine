"""FastAPI application entrypoint."""

from __future__ import annotations

from aarogya_core.logging import configure_logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings
from app.middleware import RequestIdMiddleware
from app.routers import evaluate, health, models, ocr, train, version

settings = get_settings()
configure_logging(level=settings.log_level, json_logs=settings.app_env != "development")

app = FastAPI(
    title="Aarogya AI Research Platform — Inference API",
    version=settings.api_version,
    description="Thin HTTP edge over the Research Core. Not a product API.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestIdMiddleware)

API_PREFIX = "/api/v1"
app.include_router(health.router, prefix=API_PREFIX, tags=["health"])
app.include_router(version.router, prefix=API_PREFIX, tags=["version"])
app.include_router(ocr.router, prefix=API_PREFIX, tags=["ocr"])
app.include_router(train.router, prefix=API_PREFIX, tags=["train"])
app.include_router(evaluate.router, prefix=API_PREFIX, tags=["evaluate"])
app.include_router(models.router, prefix=API_PREFIX, tags=["models"])
