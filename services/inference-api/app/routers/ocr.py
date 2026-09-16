"""OCR endpoint placeholder."""

from __future__ import annotations

from aarogya_core.types.ocr import OCRRequest, OCRResult
from fastapi import APIRouter

from app.services import OCRService

router = APIRouter()
_service = OCRService()


@router.post("/ocr", response_model=OCRResult)
def run_ocr(request: OCRRequest) -> OCRResult:
    """Future OCR endpoint — returns explicit not_implemented via StubOCRPipeline."""
    return _service.run(request)
