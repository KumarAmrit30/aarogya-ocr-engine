"""Benchmark configuration models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from aarogya_core.types.ids import DatasetId, PipelineId


class PipelinePredictionSet(BaseModel):
    """Precomputed predictions for one pipeline (no OCR)."""

    pipeline_id: PipelineId
    predictions: list[dict[str, Any]] = Field(default_factory=list)


class BenchmarkConfig(BaseModel):
    suite: str = "handwritten"
    dataset_id: DatasetId
    dataset_version: str = "v1"
    metrics: list[str] = Field(default_factory=lambda: ["cer", "wer", "exact_match"])
    primary_metric: str = "cer"
    # lower_is_better for CER/WER
    lower_is_better: bool = True
    pipeline_sets: list[PipelinePredictionSet] = Field(default_factory=list)
    references: list[dict[str, Any]] = Field(default_factory=list)
    extras: dict[str, Any] = Field(default_factory=dict)
