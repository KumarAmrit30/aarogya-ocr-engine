"""paddle recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class PaddleRecognizer:
    """Stub Recognizer for the paddle engine system."""

    engine_id = "paddle"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("paddle recognizer is not implemented yet")
