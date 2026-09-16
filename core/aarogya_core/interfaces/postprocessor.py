"""Postprocessing interface."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.ocr import OCRResult


@runtime_checkable
class Postprocessor(Protocol):
    """Normalize or enrich OCR results after recognition."""

    engine_id: str

    def postprocess(self, result: OCRResult) -> OCRResult:
        ...
