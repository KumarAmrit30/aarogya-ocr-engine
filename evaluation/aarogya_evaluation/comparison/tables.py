"""Build ComparisonResult tables."""

from __future__ import annotations

from typing import Literal

from aarogya_core.types.evaluation import ComparisonResult, EvaluationSummary


def compare_summaries(
    labeled: dict[str, EvaluationSummary],
    *,
    dimension: Literal[
        "experiment", "model", "dataset", "pipeline", "metric", "version"
    ] = "pipeline",
    metric: str = "cer",
) -> ComparisonResult:
    rows = []
    values: dict[str, float] = {}
    for label, summary in labeled.items():
        value = summary.metrics.get(metric)
        rows.append(
            {"label": label, "metric": metric, "value": value, **summary.metrics}
        )
        if value is not None:
            values[label] = value
    # deltas vs first label
    deltas: dict[str, float] = {}
    if values:
        baseline_key = next(iter(values))
        baseline = values[baseline_key]
        for key, val in values.items():
            deltas[key] = val - baseline
    return ComparisonResult(
        name=f"compare-{metric}",
        dimension=dimension,
        rows=rows,
        deltas=deltas,
    )
