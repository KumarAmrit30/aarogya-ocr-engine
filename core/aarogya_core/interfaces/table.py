"""Table extraction interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class TableExtractor(Protocol):
    """Extract tables from document images. Engines may no-op."""

    engine_id: str

    def extract_tables(self, image: Any) -> list[dict[str, Any]]: ...
