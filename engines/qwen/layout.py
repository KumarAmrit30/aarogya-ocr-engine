"""qwen layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class QwenLayoutAnalyzer:
    """Stub LayoutAnalyzer for the qwen engine system."""

    engine_id = "qwen"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("qwen layout analyzer is not implemented yet")
