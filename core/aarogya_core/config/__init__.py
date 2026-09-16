"""Platform path / settings helpers."""

from __future__ import annotations

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from aarogya_core.errors import ConfigError


class CoreSettings(BaseSettings):
    """Environment-driven paths for the Research Core."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    aarogya_repo_root: Path = Field(default=Path("."), alias="AAROGYA_REPO_ROOT")
    aarogya_datasets_dir: str = Field(default="datasets", alias="AAROGYA_DATASETS_DIR")
    aarogya_registry_dir: str = Field(default="registry", alias="AAROGYA_REGISTRY_DIR")
    aarogya_configs_dir: str = Field(default="configs", alias="AAROGYA_CONFIGS_DIR")
    aarogya_lab_dir: str = Field(default="lab", alias="AAROGYA_LAB_DIR")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    def repo_root(self) -> Path:
        root = self.aarogya_repo_root
        if not root.is_absolute():
            # Prefer walking up from CWD to find marker files
            cwd = Path.cwd()
            for candidate in [cwd, *cwd.parents]:
                if (candidate / "datasets" / "registry.yaml").exists() or (
                    candidate / "core" / "pyproject.toml"
                ).exists():
                    return candidate
            return (cwd / root).resolve()
        return root.resolve()

    def datasets_path(self) -> Path:
        return self.repo_root() / self.aarogya_datasets_dir

    def registry_path(self) -> Path:
        return self.repo_root() / self.aarogya_registry_dir

    def configs_path(self) -> Path:
        return self.repo_root() / self.aarogya_configs_dir

    def lab_path(self) -> Path:
        return self.repo_root() / self.aarogya_lab_dir


def get_settings() -> CoreSettings:
    return CoreSettings()


def resolve_repo_path(
    relative: str | Path, settings: CoreSettings | None = None
) -> Path:
    """Resolve a path relative to the repo root. Rejects empty paths."""
    settings = settings or get_settings()
    path = Path(relative)
    if path.is_absolute():
        return path
    if str(path) in ("", "."):
        raise ConfigError("Empty path is not allowed")
    return (settings.repo_root() / path).resolve()


def env_or_default(key: str, default: str) -> str:
    return os.environ.get(key, default)
