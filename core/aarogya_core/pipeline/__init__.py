"""Pipeline objects — the unit researchers swap and benchmark."""

from aarogya_core.pipeline.base import BasePipeline
from aarogya_core.pipeline.compose import compose_pipeline
from aarogya_core.pipeline.ocr_pipeline import StubOCRPipeline

__all__ = [
    "BasePipeline",
    "StubOCRPipeline",
    "compose_pipeline",
]
