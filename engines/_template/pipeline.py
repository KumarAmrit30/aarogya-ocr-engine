"""Template pipeline factory (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.pipeline.base import BasePipeline
from aarogya_core.pipeline.ocr_pipeline import StubOCRPipeline


def build_pipeline(config: dict[str, Any] | None = None) -> BasePipeline:
    """
    Return a pipeline for this engine.

    Foundation: returns StubOCRPipeline tagged with this engine_id.
    Replace with real composition when SDKs are wired.
    """
    _ = config
    pipeline = StubOCRPipeline()
    pipeline.engine_id = "template"
    return pipeline
