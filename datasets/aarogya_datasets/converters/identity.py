"""Identity converter — passes DatasetSample lists through."""

from __future__ import annotations

from typing import Any

from aarogya_core.types.data_platform import DatasetSample
from aarogya_datasets.converters.base import AnnotationFormat
from aarogya_datasets.converters.registry import register_converter


@register_converter
class IdentityConverter:
    name = "identity"
    format = AnnotationFormat.OTHER

    def convert(self, raw: Any) -> list[DatasetSample]:
        if isinstance(raw, list):
            return [
                s if isinstance(s, DatasetSample) else DatasetSample.model_validate(s)
                for s in raw
            ]
        raise TypeError("IdentityConverter expects list[DatasetSample]")
