"""
Thin export surface for evaluation.

Evaluation may import DatasetManifest / DatasetSample from aarogya_core.types
and load manifests via these helpers — never loaders/validators/pipeline.
"""

from __future__ import annotations

import json
from pathlib import Path

from aarogya_core.types.data_platform import DatasetManifest


def load_manifest(path: Path) -> DatasetManifest:
    data = json.loads(path.read_text(encoding="utf-8"))
    return DatasetManifest.model_validate(data)


__all__ = ["load_manifest"]
