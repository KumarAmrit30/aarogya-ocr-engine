"""Benchmark runner entry (re-exports package implementation)."""

from aarogya_benchmarks.runner import PipelineBenchmarkRunner

# Keep historical name as alias
StubBenchmarkRunner = PipelineBenchmarkRunner

__all__ = ["PipelineBenchmarkRunner", "StubBenchmarkRunner"]
