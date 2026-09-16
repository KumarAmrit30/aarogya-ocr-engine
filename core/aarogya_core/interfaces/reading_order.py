"""Reading order interface."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.ocr import OCRLine


@runtime_checkable
class ReadingOrder(Protocol):
    """Sort recognized lines into reading order."""

    engine_id: str

    def order(self, lines: list[OCRLine]) -> list[OCRLine]: ...
