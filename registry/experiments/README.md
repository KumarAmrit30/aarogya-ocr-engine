# Experiment registry (immutable)

**Never edit an allocated `EXP-#####`.** Reruns create a new ID.

```text
registry/experiments/EXP-00015/
  EXP-00015.yaml   # frozen metadata
  config/          # snapshotted config
  results/         # metrics JSON
  report/          # EvaluationReport exports
  artifacts/       # gitignored blobs
```

Use `aarogya_core.registry.write_experiment` — it refuses overwrite.

See `docs/adr/ADR-0004-experiments-are-immutable.md`.
