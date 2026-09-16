"""Stable registry identifiers."""

from typing import Annotated

from pydantic import Field, StringConstraints

ExperimentId = Annotated[
    str,
    StringConstraints(pattern=r"^EXP-\d{5}$"),
    Field(description="Experiment ID, e.g. EXP-00001"),
]

DatasetId = Annotated[
    str,
    StringConstraints(pattern=r"^DATASET-\d{5}$"),
    Field(description="Dataset ID, e.g. DATASET-00001"),
]

ModelId = Annotated[
    str,
    StringConstraints(pattern=r"^MODEL-\d{5}$"),
    Field(description="Model ID, e.g. MODEL-00001"),
]

AssetId = Annotated[
    str,
    StringConstraints(pattern=r"^ASSET-\d{5}$"),
    Field(description="Asset ID, e.g. ASSET-00001"),
]

PipelineId = Annotated[
    str,
    StringConstraints(pattern=r"^PIPELINE-\d{5}$"),
    Field(description="Pipeline ID, e.g. PIPELINE-00001"),
]
