"""Benchmark runner / leaderboard tests."""

from aarogya_benchmarks.config import BenchmarkConfig, PipelinePredictionSet
from aarogya_benchmarks.runner import PipelineBenchmarkRunner


def test_pipeline_leaderboard() -> None:
    refs = [{"sample_id": "1", "text": "hello"}, {"sample_id": "2", "text": "world"}]
    cfg = BenchmarkConfig(
        suite="handwritten",
        dataset_id="DATASET-00001",
        dataset_version="v1",
        metrics=["cer", "exact_match"],
        primary_metric="cer",
        references=refs,
        pipeline_sets=[
            PipelinePredictionSet(
                pipeline_id="PIPELINE-00001",
                predictions=[
                    {"sample_id": "1", "text": "hello"},
                    {"sample_id": "2", "text": "world"},
                ],
            ),
            PipelinePredictionSet(
                pipeline_id="PIPELINE-00002",
                predictions=[
                    {"sample_id": "1", "text": "hallo"},
                    {"sample_id": "2", "text": "world"},
                ],
            ),
        ],
    )
    suite = PipelineBenchmarkRunner().run(cfg)
    assert len(suite.runs) == 2
    assert suite.leaderboard[0]["pipeline_id"] == "PIPELINE-00001"
    assert suite.comparison is not None
    assert "PIPELINE-00001" in suite.comparison.deltas
