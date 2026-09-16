# Registry

## ID scheme

| Entity | Pattern | Location |
|--------|---------|----------|
| Experiment | `EXP-#####` | `registry/experiments/EXP-#####/` (**immutable**) |
| Dataset | `DATASET-#####` | `datasets/registry.yaml` (+ versions `v1`…) |
| Model | `MODEL-#####` | `registry/models/` |
| Asset | `ASSET-#####` | `assets/registry.yaml` |
| Pipeline | `PIPELINE-#####` | `registry/pipelines/` |

Allocate: `aarogya_core.registry.next_id`.

## Dataset versions

`Dataset → Version → Split`. Evaluation cites `dataset_id` + `dataset_version`.

## Assets vs models

Logical model (`MODEL`) ≠ files on disk (`ASSET`: checkpoints, tokenizers, ONNX, …).

## Pipelines

Benchmark compositions of adapters. See ADR-0002.

## Immutable experiments

`write_experiment` refuses overwrite. Rerun → new `EXP-#####`. See ADR-0004.
