# Dataset Validation

Structural checks only (`aarogya_datasets.validators`):

- duplicate sample IDs
- empty annotations (warning)
- missing image assets (warning)
- invalid UTF-8 text

Output: `DatasetValidationReport` (`passed` + `issues`).

**Not** blur/contrast/writer diversity — those belong in quality.
