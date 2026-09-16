"""Train endpoint placeholder."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas import PlaceholderResponse, TrainRequest
from app.services import TrainService

router = APIRouter()
_service = TrainService()


@router.post("/train", response_model=PlaceholderResponse)
def train(request: TrainRequest) -> PlaceholderResponse:
    return _service.run(request)
