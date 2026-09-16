"""gemini layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class GeminiLayoutAnalyzer:
    """Stub LayoutAnalyzer for the gemini engine system."""

    engine_id = "gemini"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("gemini layout analyzer is not implemented yet")
