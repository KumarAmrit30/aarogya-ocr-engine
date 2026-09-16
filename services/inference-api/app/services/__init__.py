"""Service stubs."""

from __future__ import annotations

from aarogya_core.pipeline import StubOCRPipeline, compose_pipeline
from aarogya_core.types.ocr import OCRRequest, OCRResult

from app.schemas import PlaceholderResponse


class OCRService:
    """Delegates to core Pipeline stub — no OCR logic."""

    def __init__(self) -> None:
        self._pipeline = StubOCRPipeline()

    def run(self, request: OCRRequest) -> OCRResult:
        pipeline = compose_pipeline(engine_id=request.engine_id or "stub")
        return pipeline.run(request)


class TrainService:
    def run(self, *_args: object, **_kwargs: object) -> PlaceholderResponse:
        return PlaceholderResponse(
            message="Training endpoint is a placeholder. Implement TrainingRunner next."
        )


class EvaluateService:
    def run(self, *_args: object, **_kwargs: object) -> PlaceholderResponse:
        return PlaceholderResponse(
            message="Evaluate endpoint is a placeholder. Implement EvaluationRunner next."
        )


class ModelService:
    def list_models(self) -> list[object]:
        return []
