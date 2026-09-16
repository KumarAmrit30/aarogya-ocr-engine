"""Version endpoint."""

from __future__ import annotations

import os

from fastapi import APIRouter

from app.config.settings import get_settings
from app.schemas import VersionResponse

router = APIRouter()


@router.get("/version", response_model=VersionResponse)
def version() -> VersionResponse:
    settings = get_settings()
    return VersionResponse(
        version=settings.api_version,
        api_schema_version=settings.api_schema_version,
        git_sha=os.environ.get("GIT_SHA"),
    )
