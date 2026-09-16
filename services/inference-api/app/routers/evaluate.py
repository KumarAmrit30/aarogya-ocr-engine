"""Evaluate endpoint placeholder."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas import EvaluateRequest, PlaceholderResponse
from app.services import EvaluateService

router = APIRouter()
_service = EvaluateService()


@router.post("/evaluate", response_model=PlaceholderResponse)
def evaluate(request: EvaluateRequest) -> PlaceholderResponse:
    return _service.run(request)
