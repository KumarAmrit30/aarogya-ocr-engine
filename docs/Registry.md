# Registry

## ID scheme

| Entity | Pattern | Catalog |
|--------|---------|---------|
| Experiment | `EXP-#####` | `registry/experiments/` |
| Dataset | `DATASET-#####` | **`datasets/registry.yaml`** (authoritative) |
| Model | `MODEL-#####` | `registry/models/` |

Allocate with:

```python
from aarogya_core.registry import next_id, list_registry_ids
from pathlib import Path

ids = list_registry_ids(Path("registry/experiments"), "EXP")
print(next_id("EXP", ids))
```

## Dataset fields

`dataset_id`, `name`, `version`, `license`, `language`, `writer_count`, `source`, `quality`, `split`, `path`, `card`

## Avoid duplication

Do not copy full dataset metadata into `registry/datasets/`. Optional index files may point at `datasets/registry.yaml` only.
