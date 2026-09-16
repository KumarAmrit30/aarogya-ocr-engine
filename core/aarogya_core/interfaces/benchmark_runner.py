"""Comparative benchmark runner interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.evaluation import BenchmarkSuite
from aarogya_core.types.metrics import Metrics


@runtime_checkable
class BenchmarkRunner(Protocol):
    """
    Run comparative benchmarks across pipelines × dataset versions.

    Must not import engine packages; consumes precomputed predictions.
    """

    suite: str

    def run(self, config: dict[str, Any]) -> list[Metrics] | BenchmarkSuite: ...
