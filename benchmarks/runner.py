"""Benchmark runner stub (no real benchmarking yet)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.metrics import Metrics


class StubBenchmarkRunner:
    """Placeholder comparative benchmark runner."""

    suite = "stub"

    def run(self, config: dict[str, Any]) -> list[Metrics]:
        raise NotImplementedComponentError(
            "Benchmark runner is not implemented yet. "
            "Define suites under benchmarks/<suite>/ and wire engines."
        )
