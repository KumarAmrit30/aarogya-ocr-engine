"""trocr layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class TrocrLayoutAnalyzer:
    """Stub LayoutAnalyzer for the trocr engine system."""

    engine_id = "trocr"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("trocr layout analyzer is not implemented yet")
