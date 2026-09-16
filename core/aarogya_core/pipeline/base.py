"""Base pipeline helpers."""

from __future__ import annotations

from abc import ABC, abstractmethod

from aarogya_core.types.ocr import OCRRequest, OCRResult


class BasePipeline(ABC):
    """Abstract base for OCR-style pipelines."""

    engine_id: str = "unknown"
    config_hash: str | None = None

    @abstractmethod
    def run(self, request: OCRRequest) -> OCRResult:
        """Execute the full pipeline."""

    def steps(self) -> list[str]:
        return ["preprocess", "detect", "recognize", "reading_order", "postprocess"]
