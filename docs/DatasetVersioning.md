# Dataset Versioning

Published versions are **immutable**. Re-publishing the same `VERSION-#####` directory raises `RegistryError`.

Human labels (`v1`, `v2`) map to stable `version_id` (`VERSION-#####`).

Each version stores fingerprint, validation, quality, statistics, card, lineage, and provenance.
