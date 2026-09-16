"""Text recognition (HTR / OCR) interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ocr import OCRLine


@runtime_checkable
class Recognizer(Protocol):
    """Recognize text within cropped regions or full images."""

    engine_id: str

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        """Return recognized lines."""
        ...
