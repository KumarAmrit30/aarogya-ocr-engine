# Dataset Lineage

Dataset-level DAG (`DatasetLineageGraph` / `LineageEdge`):

Relations: `converted | canonicalized | augmented | filtered | split | published | derived`.

Stored as `lineage.yaml` under each published version.

Sample-level history uses append-only `SampleProvenance` (separate).
