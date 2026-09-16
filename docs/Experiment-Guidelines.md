# Experiment guidelines

1. State a hypothesis in `research/hypotheses/` **before** training/eval.
2. Allocate `EXP-#####` and write `registry/experiments/EXP-#####.yaml`.
3. Snapshot config under `configs/` and record `config_hash` in logs.
4. Link datasets (`DATASET-#####`) and models (`MODEL-#####`).
5. On completion or abandonment, write a finding or failure note.
6. Promote reusable code from `lab/` into `engines/` / `core/` deliberately.

Artifact path convention:

```text
registry/experiments/EXP-00001/
  EXP-00001.yaml   # or sibling YAML in registry/experiments/
  artifacts/       # gitignored blobs
```
