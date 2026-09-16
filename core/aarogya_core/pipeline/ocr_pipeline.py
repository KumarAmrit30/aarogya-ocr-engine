"""Stub OCR pipeline — explicit not_implemented, no fake OCR."""

from __future__ import annotations

from aarogya_core.pipeline.base import BasePipeline
from aarogya_core.types.ocr import OCRRequest, OCRResult, PipelineStatus


class StubOCRPipeline(BasePipeline):
    """Foundation placeholder. Does not perform OCR."""

    engine_id = "stub"

    def run(self, request: OCRRequest) -> OCRResult:
        engine = request.engine_id or self.engine_id
        return OCRResult(
            status=PipelineStatus.NOT_IMPLEMENTED,
            message=(
                "OCR pipeline is not implemented yet. "
                "Wire an engine adapter under engines/<name>/ and compose via core.pipeline."
            ),
            engine_id=engine,
            config_hash=self.config_hash,
            metadata={"requested_engine": request.engine_id},
        )
