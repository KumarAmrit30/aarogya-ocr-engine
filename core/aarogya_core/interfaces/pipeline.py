"""Pipeline Protocol — the unit researchers swap and benchmark."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.ocr import OCRRequest, OCRResult


@runtime_checkable
class Pipeline(Protocol):
    """Composable inference pipeline."""

    engine_id: str
    config_hash: str | None

    def run(self, request: OCRRequest) -> OCRResult:
        """Execute the full pipeline."""
        ...

    def steps(self) -> list[str]:
        """Return ordered step names for observability."""
        ...
