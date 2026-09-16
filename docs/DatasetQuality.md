# Dataset Quality

Research goodness (`aarogya_datasets.quality`), separate from validators:

- short annotations
- duplicate text ratios
- writer diversity
- vision placeholders (`blur_score`, `contrast`, … return `-1` until implemented)

Output: `DatasetQualityReport` with `overall_score` and `metrics`.

Pipeline runs quality **after** validation and may skip if validation failed.
