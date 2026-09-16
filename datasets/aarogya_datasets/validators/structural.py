"""Structural validators — NOT quality analyzers."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetSample, DatasetValidationIssue
from aarogya_datasets.validators.registry import register_validator


@register_validator
class DuplicateIdValidator:
    name = "duplicate_ids"

    def validate(self, samples: list[DatasetSample]) -> list[DatasetValidationIssue]:
        seen: set[str] = set()
        issues: list[DatasetValidationIssue] = []
        for s in samples:
            sid = str(s.sample_id)
            if sid in seen:
                issues.append(
                    DatasetValidationIssue(
                        code="duplicate_id",
                        message=f"Duplicate sample_id {sid}",
                        sample_id=sid,
                    )
                )
            seen.add(sid)
        return issues


@register_validator
class EmptyAnnotationValidator:
    name = "empty_annotations"

    def validate(self, samples: list[DatasetSample]) -> list[DatasetValidationIssue]:
        issues: list[DatasetValidationIssue] = []
        for s in samples:
            if not (s.text or s.lines or s.words):
                issues.append(
                    DatasetValidationIssue(
                        code="empty_annotation",
                        message="Empty text/lines/words",
                        sample_id=str(s.sample_id),
                        severity="warning",
                    )
                )
        return issues


@register_validator
class MissingImageValidator:
    name = "missing_image"

    def validate(self, samples: list[DatasetSample]) -> list[DatasetValidationIssue]:
        issues: list[DatasetValidationIssue] = []
        for s in samples:
            if s.image is None or not s.image.uri:
                issues.append(
                    DatasetValidationIssue(
                        code="missing_image",
                        message="Sample missing image asset",
                        sample_id=str(s.sample_id),
                        severity="warning",
                    )
                )
        return issues


@register_validator
class InvalidUtfValidator:
    name = "invalid_utf"

    def validate(self, samples: list[DatasetSample]) -> list[DatasetValidationIssue]:
        issues: list[DatasetValidationIssue] = []
        for s in samples:
            try:
                s.text.encode("utf-8")
            except UnicodeError:
                issues.append(
                    DatasetValidationIssue(
                        code="invalid_utf",
                        message="Text is not valid UTF-8",
                        sample_id=str(s.sample_id),
                    )
                )
        return issues
