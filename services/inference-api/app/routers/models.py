"""Models list placeholder."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas import ModelListResponse
from app.services import ModelService

router = APIRouter()
_service = ModelService()


@router.get("/models", response_model=ModelListResponse)
def list_models() -> ModelListResponse:
    models = _service.list_models()
    return ModelListResponse(models=list(models))  # type: ignore[arg-type]
