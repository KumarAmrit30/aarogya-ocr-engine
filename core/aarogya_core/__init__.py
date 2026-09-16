"""Aarogya Research Core — shared types, interfaces, pipelines, and registry."""

from aarogya_core.types.common import SCHEMA_VERSION
from aarogya_core.types.ids import AssetId, DatasetId, ExperimentId, ModelId, PipelineId

__all__ = [
    "SCHEMA_VERSION",
    "DatasetId",
    "ExperimentId",
    "ModelId",
    "AssetId",
    "PipelineId",
]

__version__ = "0.1.0"
