"""Benchmark-level comparison wrappers."""

from __future__ import annotations

from aarogya_core.types.evaluation import (
    BenchmarkSuite,
    ComparisonResult,
    EvaluationSummary,
)
from aarogya_evaluation.comparison.tables import compare_summaries


def compare_suite_by_pipeline(
    suite: BenchmarkSuite, *, metric: str = "cer"
) -> ComparisonResult:
    labeled: dict[str, EvaluationSummary] = {}
    for run in suite.runs:
        if run.summary is not None:
            labeled[str(run.pipeline_id)] = run.summary
    return compare_summaries(labeled, dimension="pipeline", metric=metric)
