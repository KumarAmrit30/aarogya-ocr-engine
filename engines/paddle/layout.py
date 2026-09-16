"""paddle layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class PaddleLayoutAnalyzer:
    """Stub LayoutAnalyzer for the paddle engine system."""

    engine_id = "paddle"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("paddle layout analyzer is not implemented yet")
