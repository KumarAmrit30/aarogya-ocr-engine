"""Registry loaders and ID helpers."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from aarogya_core.errors import RegistryError
from aarogya_core.types.dataset import DatasetRecord

ID_PATTERNS = {
    "EXP": re.compile(r"^EXP-(\d{5})$"),
    "DATASET": re.compile(r"^DATASET-(\d{5})$"),
    "MODEL": re.compile(r"^MODEL-(\d{5})$"),
}


def next_id(prefix: str, existing: list[str]) -> str:
    """Allocate the next sequential ID for EXP / DATASET / MODEL."""
    prefix = prefix.upper().rstrip("-")
    if prefix not in ID_PATTERNS:
        raise RegistryError(f"Unknown ID prefix: {prefix}")
    pattern = ID_PATTERNS[prefix]
    max_n = 0
    for item in existing:
        match = pattern.match(item)
        if match:
            max_n = max(max_n, int(match.group(1)))
    return f"{prefix}-{max_n + 1:05d}"


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise RegistryError(f"Registry file not found: {path}")
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_dataset_registry(path: Path) -> list[DatasetRecord]:
    """Load datasets/registry.yaml into typed records."""
    data = load_yaml(path)
    entries = data.get("datasets", data if isinstance(data, list) else [])
    if not isinstance(entries, list):
        raise RegistryError("datasets/registry.yaml must contain a 'datasets' list")
    return [DatasetRecord.model_validate(item) for item in entries]


def list_registry_ids(directory: Path, prefix: str) -> list[str]:
    """List IDs from YAML filenames like EXP-00001.yaml."""
    if not directory.exists():
        return []
    ids: list[str] = []
    pattern = ID_PATTERNS[prefix.upper().rstrip("-")]
    for path in sorted(directory.glob("*.yaml")):
        stem = path.stem
        if pattern.match(stem):
            ids.append(stem)
    return ids
