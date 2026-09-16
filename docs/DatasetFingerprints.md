# Dataset Fingerprints

`DatasetFingerprint` = SHA-256 over:

- sample ids + texts
- splits
- statistics values
- dataset/version ids

Stable across recomputation for the same inputs. Prefer recording fingerprints on experiments for reproducibility.
