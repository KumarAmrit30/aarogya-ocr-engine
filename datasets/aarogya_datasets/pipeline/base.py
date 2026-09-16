"""DatasetPipeline Protocol."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.data_platform import DatasetSource, PublishedVersionResult


@runtime_checkable
class DatasetPipeline(Protocol):
    """Executable ingest orchestrator (like OCR Pipeline)."""

    def run(
        self, source: DatasetSource, config: dict[str, Any] | None = None
    ) -> PublishedVersionResult: ...
