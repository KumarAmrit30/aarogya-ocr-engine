"""florence layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class FlorenceLayoutAnalyzer:
    """Stub LayoutAnalyzer for the florence engine system."""

    engine_id = "florence"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("florence layout analyzer is not implemented yet")
