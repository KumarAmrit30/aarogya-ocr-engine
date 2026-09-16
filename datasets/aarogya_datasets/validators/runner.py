"""Run all registered structural validators."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetSample, DatasetValidationReport
from aarogya_core.types.ids import DatasetId, VersionId
from aarogya_datasets.validators import structural  # noqa: F401
from aarogya_datasets.validators.registry import get_validator, list_validators


def run_validators(
    samples: list[DatasetSample],
    *,
    dataset_id: DatasetId | None = None,
    version_id: VersionId | None = None,
    names: list[str] | None = None,
) -> DatasetValidationReport:
    names = names or list_validators()
    issues = []
    for name in names:
        issues.extend(get_validator(name).validate(samples))
    errors = [i for i in issues if i.severity == "error"]
    return DatasetValidationReport(
        dataset_id=dataset_id,
        version_id=version_id,
        passed=len(errors) == 0,
        issues=issues,
    )
