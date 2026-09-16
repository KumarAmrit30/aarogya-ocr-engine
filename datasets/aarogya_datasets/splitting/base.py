"""Split strategy Protocol — placeholders only."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.data_platform import DatasetSample, DatasetSplit


@runtime_checkable
class SplitStrategy(Protocol):
    name: str

    def split(self, samples: list[DatasetSample]) -> list[DatasetSplit]: ...


class _Stub:
    name = "stub"

    def split(self, samples: list[DatasetSample]) -> list[DatasetSplit]:
        raise NotImplementedComponentError(f"{self.name} split not implemented")


class RandomSplit(_Stub):
    name = "random"


class WriterSplit(_Stub):
    name = "writer"


class ClinicSplit(_Stub):
    name = "clinic"


class PatientSplit(_Stub):
    name = "patient"


class CustomSplit(_Stub):
    name = "custom"
