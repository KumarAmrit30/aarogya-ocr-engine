# Dataset Architecture

## Packages

| Area | Package / module |
|------|------------------|
| Domain types | `aarogya_core.types.data_platform` + `media_asset.Asset` |
| Orchestrator | `aarogya_datasets.pipeline` |
| I/O | `aarogya_datasets.storage` (`StorageBackend`, `LocalStorage`) |
| Structure checks | `aarogya_datasets.validators` |
| Research goodness | `aarogya_datasets.quality` |
| Eval-facing export | `aarogya_datasets.exports` / core types only |

## Asset-first samples

`DatasetSample.image` / `.annotation` are `Asset` objects (`uri`, `checksum`, `mime`, `backend`) — not bare paths as the primary API.

## Validation ≠ Quality

Validators answer “is it structurally valid?”. Quality answers “is it good for research?”. Never merge packages.

## Lineage + provenance

- **SampleProvenance** — per-sample append-only audit
- **DatasetLineageGraph** — dataset-level DAG (`converted`, `published`, …)

## Fingerprints

`DatasetFingerprint` hashes manifest samples/splits + statistics. Experiments should record fingerprints, not version IDs alone.

## Evaluation boundary

```
evaluation  --reads-->  DatasetManifest + DatasetSample (+ fingerprint)
evaluation  --MUST NOT import-->  loaders, validators, quality, cards, pipeline
```
