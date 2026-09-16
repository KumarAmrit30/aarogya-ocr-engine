"""Pluggable metrics — import registers all implementations."""

from aarogya_evaluation.metrics import (  # noqa: F401
    cer,
    character_accuracy,
    document_accuracy,
    exact_match,
    line_accuracy,
    normalized_cer,
    normalized_wer,
    page_accuracy,
    placeholders,
    wer,
    word_accuracy,
)
from aarogya_evaluation.metrics.factory import create_metric, create_metrics
from aarogya_evaluation.metrics.registry import list_metrics
from aarogya_evaluation.metrics.runner import MetricRunner

__all__ = [
    "MetricRunner",
    "create_metric",
    "create_metrics",
    "list_metrics",
]
