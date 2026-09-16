"""Shared domain types for the Aarogya AI Research Platform."""

from aarogya_core.types.common import SCHEMA_VERSION, BoundingBox, SchemaVersionMixin
from aarogya_core.types.dataset import DatasetRecord
from aarogya_core.types.experiment import Experiment
from aarogya_core.types.ids import DatasetId, ExperimentId, ModelId
from aarogya_core.types.metrics import Metrics
from aarogya_core.types.model import ModelRecord
from aarogya_core.types.ocr import OCRLine, OCRRequest, OCRResult, OCRWord, PipelineStatus

__all__ = [
    "SCHEMA_VERSION",
    "BoundingBox",
    "SchemaVersionMixin",
    "DatasetId",
    "ExperimentId",
    "ModelId",
    "OCRWord",
    "OCRLine",
    "OCRRequest",
    "OCRResult",
    "PipelineStatus",
    "Metrics",
    "Experiment",
    "DatasetRecord",
    "ModelRecord",
]
