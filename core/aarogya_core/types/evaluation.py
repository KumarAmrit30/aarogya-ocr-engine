"""Evaluation domain types — model-agnostic GT / Prediction / reports."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import DatasetId, ExperimentId, ModelId, PipelineId
from aarogya_core.types.metrics import Metrics


class GroundTruth(SchemaVersionMixin):
    """Reference annotation for one evaluation sample."""

    sample_id: str
    text: str = ""
    lines: list[str] = Field(default_factory=list)
    words: list[str] = Field(default_factory=list)
    entities: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)


class Prediction(SchemaVersionMixin):
    """Model/pipeline output for one sample. Engine packages stay opaque."""

    sample_id: str
    text: str = ""
    lines: list[str] = Field(default_factory=list)
    words: list[str] = Field(default_factory=list)
    entities: dict[str, Any] = Field(default_factory=dict)
    pipeline_id: PipelineId | None = None
    engine_id: str | None = None
    model_id: ModelId | None = None
    latency_ms: float | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class MetricResult(SchemaVersionMixin):
    """Result of a single metric on one sample or an aggregate."""

    name: str
    value: float | None = None
    implemented: bool = True
    normalization: str | None = None
    sample_id: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)
    message: str | None = None


class EvaluationSummary(SchemaVersionMixin):
    """Aggregated metrics for a full evaluation run."""

    metrics: dict[str, float] = Field(default_factory=dict)
    sample_count: int = 0
    duration_seconds: float = 0.0
    primary_metric: str = "cer"
    extras: dict[str, Any] = Field(default_factory=dict)

    def to_metrics(self, name: str = "evaluation") -> Metrics:
        return Metrics(name=name, values=dict(self.metrics), extras=dict(self.extras))


class FailureCase(SchemaVersionMixin):
    """One recorded failure for analysis."""

    sample_id: str
    category: str = "unknown"
    reference: str | None = None
    prediction: str | None = None
    notes: str | None = None
    metric_name: str | None = None
    metric_value: float | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class SampleEvaluation(BaseModel):
    """Per-sample metric bundle."""

    sample_id: str
    results: list[MetricResult] = Field(default_factory=list)
    failure: FailureCase | None = None


class EvaluationConfig(SchemaVersionMixin):
    """Configuration for an evaluation run."""

    metrics: list[str] = Field(default_factory=lambda: ["cer", "wer", "exact_match"])
    normalization: str | None = Field(
        default=None,
        description="Global override; else each metric's required_normalization",
    )
    primary_metric: str = "cer"
    collect_failures: bool = True
    dataset_id: DatasetId | None = None
    dataset_version: str | None = "v1"
    pipeline_id: PipelineId | None = None
    experiment_id: ExperimentId | None = None
    report_dir: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class EvaluationReport(SchemaVersionMixin):
    """Full evaluation artifact."""

    report_id: str
    created_at: datetime | None = None
    config: EvaluationConfig
    dataset_id: DatasetId | None = None
    dataset_version: str | None = None
    pipeline_id: PipelineId | None = None
    experiment_id: ExperimentId | None = None
    summary: EvaluationSummary
    failures: list[FailureCase] = Field(default_factory=list)
    samples: list[SampleEvaluation] = Field(default_factory=list)
    timing: dict[str, float] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)


class ComparisonResult(SchemaVersionMixin):
    """Side-by-side comparison across runs / pipelines / versions."""

    name: str
    dimension: Literal[
        "experiment",
        "model",
        "dataset",
        "pipeline",
        "metric",
        "version",
    ]
    rows: list[dict[str, Any]] = Field(default_factory=list)
    deltas: dict[str, float] = Field(default_factory=dict)
    extras: dict[str, Any] = Field(default_factory=dict)


class BenchmarkRun(SchemaVersionMixin):
    """One pipeline × dataset-version × config execution."""

    run_id: str
    pipeline_id: PipelineId
    dataset_id: DatasetId
    dataset_version: str
    config_ref: str | None = None
    summary: EvaluationSummary | None = None
    report_id: str | None = None
    status: Literal["planned", "running", "completed", "failed"] = "planned"
    extras: dict[str, Any] = Field(default_factory=dict)


class BenchmarkSuite(SchemaVersionMixin):
    """Named comparative suite with runs and leaderboard snapshot."""

    suite: str
    runs: list[BenchmarkRun] = Field(default_factory=list)
    leaderboard: list[dict[str, Any]] = Field(default_factory=list)
    comparison: ComparisonResult | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
