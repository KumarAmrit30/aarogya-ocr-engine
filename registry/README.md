# Registry

Authoritative ID catalogs for experiments, models, and dataset indexes.

## ID scheme

| Entity | Pattern | Example |
|--------|---------|---------|
| Experiment | `EXP-#####` | `EXP-00001` |
| Dataset | `DATASET-#####` | `DATASET-00003` |
| Model | `MODEL-#####` | `MODEL-00008` |

Allocate IDs with `aarogya_core.registry.next_id`.

## Layout

- `datasets/` — optional per-id YAML index pointing at `datasets/registry.yaml` entries (do not duplicate full metadata).
- `models/` — `MODEL-#####.yaml` records for trained/external checkpoints.
- `experiments/` — `EXP-#####.yaml` records; large artifacts under `artifacts/` (gitignored).

## Split of responsibility

- **Dataset catalog:** `datasets/registry.yaml`
- **Cross-entity IDs + experiment/model records:** this directory
