"""Validator Protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.data_platform import DatasetSample, DatasetValidationIssue


@runtime_checkable
class Validator(Protocol):
    name: str

    def validate(
        self, samples: list[DatasetSample]
    ) -> list[DatasetValidationIssue]: ...
