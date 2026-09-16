"""Shared domain types for the Aarogya AI Research Platform."""

from aarogya_core.types.asset import AssetRecord
from aarogya_core.types.common import SCHEMA_VERSION, BoundingBox, SchemaVersionMixin
from aarogya_core.types.dataset import DatasetRecord, DatasetVersion
from aarogya_core.types.evaluation import (
    BenchmarkRun,
    BenchmarkSuite,
    ComparisonResult,
    EvaluationConfig,
    EvaluationReport,
    EvaluationSummary,
    FailureCase,
    GroundTruth,
    MetricResult,
    Prediction,
    SampleEvaluation,
)
from aarogya_core.types.experiment import (
    ConfigRef,
    Experiment,
    ExperimentArtifactLayout,
)
from aarogya_core.types.ids import AssetId, DatasetId, ExperimentId, ModelId, PipelineId
from aarogya_core.types.metrics import Metrics
from aarogya_core.types.model import ModelRecord
from aarogya_core.types.ocr import (
    OCRLine,
    OCRRequest,
    OCRResult,
    OCRWord,
    PipelineStatus,
)
from aarogya_core.types.pipeline import PipelineRecord, PipelineStep

__all__ = [
    "SCHEMA_VERSION",
    "BoundingBox",
    "SchemaVersionMixin",
    "DatasetId",
    "ExperimentId",
    "ModelId",
    "AssetId",
    "PipelineId",
    "OCRWord",
    "OCRLine",
    "OCRRequest",
    "OCRResult",
    "PipelineStatus",
    "Metrics",
    "Experiment",
    "ExperimentArtifactLayout",
    "ConfigRef",
    "DatasetRecord",
    "DatasetVersion",
    "ModelRecord",
    "AssetRecord",
    "PipelineRecord",
    "PipelineStep",
    "GroundTruth",
    "Prediction",
    "MetricResult",
    "EvaluationSummary",
    "EvaluationConfig",
    "EvaluationReport",
    "FailureCase",
    "SampleEvaluation",
    "ComparisonResult",
    "BenchmarkRun",
    "BenchmarkSuite",
]
