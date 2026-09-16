"""trocr recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class TrocrRecognizer:
    """Stub Recognizer for the trocr engine system."""

    engine_id = "trocr"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("trocr recognizer is not implemented yet")
