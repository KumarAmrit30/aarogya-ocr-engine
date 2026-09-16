"""Document layout analysis interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class LayoutAnalyzer(Protocol):
    """Analyze page layout (blocks, columns, headers, etc.)."""

    engine_id: str

    def analyze(self, image: Any) -> dict[str, Any]: ...
