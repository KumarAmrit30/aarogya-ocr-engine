"""Metric factory and collections."""

from __future__ import annotations

from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.collection import MetricCollection
from aarogya_evaluation.metrics.registry import get_metric_class, list_metrics


def create_metric(name: str) -> BaseMetric:
    return get_metric_class(name)()


def create_metrics(names: list[str] | None = None) -> MetricCollection:
    if names is None:
        names = list_metrics(implemented_only=True)
    return MetricCollection([create_metric(n) for n in names])
