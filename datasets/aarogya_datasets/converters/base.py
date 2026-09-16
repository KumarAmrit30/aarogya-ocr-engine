"""Converter Protocol — annotation formats → DatasetSample."""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.data_platform import DatasetSample


class AnnotationFormat(StrEnum):
    TXT = "txt"
    CSV = "csv"
    JSON = "json"
    XML = "xml"
    COCO = "coco"
    YOLO = "yolo"
    ICDAR = "icdar"
    OTHER = "other"


@runtime_checkable
class Converter(Protocol):
    name: str
    format: AnnotationFormat

    def convert(self, raw: Any) -> list[DatasetSample]: ...
