# Benchmarking

Comparative evaluation across **pipelines** and **dataset versions**.

## Unit of comparison

`PIPELINE-#####` × `DATASET-#####@vN` — not bare engine names.

## Package

`aarogya_benchmarks` — `PipelineBenchmarkRunner` consumes **precomputed predictions** (no OCR).

## Example

```python
from aarogya_benchmarks.config import BenchmarkConfig, PipelinePredictionSet
from aarogya_benchmarks.runner import PipelineBenchmarkRunner

suite = PipelineBenchmarkRunner().run(
    BenchmarkConfig(
        suite="handwritten",
        dataset_id="DATASET-00001",
        dataset_version="v1",
        references=[{"sample_id": "1", "text": "hello"}],
        pipeline_sets=[
            PipelinePredictionSet(
                pipeline_id="PIPELINE-00001",
                predictions=[{"sample_id": "1", "text": "hello"}],
            )
        ],
    )
)
print(suite.leaderboard)
```

## Suites

`benchmarks/handwritten|printed|mixed|robustness|latency/`

See ADR-0002.
