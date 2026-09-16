"""Registry loaders, ID helpers, and immutable experiment writers."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from aarogya_core.errors import RegistryError
from aarogya_core.types.asset import AssetRecord
from aarogya_core.types.dataset import DatasetRecord
from aarogya_core.types.experiment import Experiment, ExperimentArtifactLayout
from aarogya_core.types.pipeline import PipelineRecord

ID_PATTERNS = {
    "EXP": re.compile(r"^EXP-(\d{5})$"),
    "DATASET": re.compile(r"^DATASET-(\d{5})$"),
    "MODEL": re.compile(r"^MODEL-(\d{5})$"),
    "ASSET": re.compile(r"^ASSET-(\d{5})$"),
    "PIPELINE": re.compile(r"^PIPELINE-(\d{5})$"),
    "VERSION": re.compile(r"^VERSION-(\d{5})$"),
    "SAMPLE": re.compile(r"^SAMPLE-(\d{5,})$"),
}


def next_id(prefix: str, existing: list[str]) -> str:
    """Allocate the next sequential ID for known prefixes."""
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


def dump_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True)


def load_dataset_registry(path: Path) -> list[DatasetRecord]:
    """Load datasets/registry.yaml into typed records."""
    data = load_yaml(path)
    entries = data.get("datasets", data if isinstance(data, list) else [])
    if not isinstance(entries, list):
        raise RegistryError("datasets/registry.yaml must contain a 'datasets' list")
    return [DatasetRecord.model_validate(item) for item in entries]


def load_asset_registry(path: Path) -> list[AssetRecord]:
    data = load_yaml(path)
    entries = data.get("assets", [])
    if not isinstance(entries, list):
        raise RegistryError("assets/registry.yaml must contain an 'assets' list")
    return [AssetRecord.model_validate(item) for item in entries]


def load_pipeline_record(path: Path) -> PipelineRecord:
    data = load_yaml(path)
    return PipelineRecord.model_validate(data)


def list_registry_ids(directory: Path, prefix: str) -> list[str]:
    """List IDs from YAML filenames or experiment directories."""
    if not directory.exists():
        return []
    ids: list[str] = []
    key = prefix.upper().rstrip("-")
    pattern = ID_PATTERNS[key]
    for path in sorted(directory.iterdir()):
        stem = path.stem if path.is_file() else path.name
        if pattern.match(stem):
            ids.append(stem)
    return ids


def experiment_dir(registry_root: Path, experiment_id: str) -> Path:
    return registry_root / "experiments" / experiment_id


def write_experiment(
    registry_root: Path,
    experiment: Experiment,
    *,
    overwrite: bool = False,
) -> Path:
    """
    Persist an immutable experiment directory.

    Raises RegistryError if the directory already exists (unless overwrite=True,
    which is reserved for tests and must not be used for production reruns).
    """
    root = experiment_dir(registry_root, experiment.experiment_id)
    if root.exists() and not overwrite:
        raise RegistryError(
            f"Experiment {experiment.experiment_id} already exists and is immutable. "
            "Allocate a new EXP-##### instead of overwriting."
        )
    layout = experiment.artifact_layout or ExperimentArtifactLayout(root=str(root))
    if experiment.artifact_layout is None:
        experiment.artifact_layout = ExperimentArtifactLayout(root=str(root))

    root.mkdir(parents=True, exist_ok=True)
    for sub in (
        layout.config_dir,
        layout.results_dir,
        layout.report_dir,
        layout.artifacts_dir,
    ):
        (root / sub).mkdir(parents=True, exist_ok=True)

    meta_path = root / f"{experiment.experiment_id}.yaml"
    dump_yaml(meta_path, experiment.model_dump(mode="json"))
    return root
