"""Medical entity / prescription parsing interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ocr import OCRResult


@runtime_checkable
class MedicalParser(Protocol):
    """Parse medical entities from OCR text / structured results."""

    engine_id: str

    def parse(self, result: OCRResult) -> dict[str, Any]:
        ...
