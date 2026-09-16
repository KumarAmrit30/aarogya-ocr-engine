# Dataset Registry

`datasets/registry.yaml` is the **catalog index** only:

- `DATASET-#####` entries with metadata
- Pointers to version dirs / cards
- No full sample lists

Published versions live under:

```text
datasets/versions/{DATASET-#####}/{VERSION-#####}/
  VERSION-#####.yaml
  manifest.json
  statistics.json
  quality.json
  validation.json
  card.md
  lineage.yaml
  provenance/
```

Optional index stubs: `registry/datasets/`, `registry/versions/`, `registry/samples/`.

IDs: `DATASET-#####`, `VERSION-#####`, `SAMPLE-#####`, `ASSET-#####`.
