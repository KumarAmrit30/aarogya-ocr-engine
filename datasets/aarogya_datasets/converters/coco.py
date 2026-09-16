"""Stub converter for COCO — not implemented."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.data_platform import DatasetSample
from aarogya_datasets.converters.base import AnnotationFormat
from aarogya_datasets.converters.registry import register_converter


@register_converter
class COCOConverter:
    name = "coco"
    format = AnnotationFormat.COCO

    def convert(self, raw: Any) -> list[DatasetSample]:
        raise NotImplementedComponentError("coco converter not implemented — Phase 4+")
