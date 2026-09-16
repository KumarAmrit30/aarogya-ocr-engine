"""Local filesystem storage backend."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


class LocalStorage:
    """StorageBackend implementation for local disk."""

    name = "local"

    def __init__(self, root: Path | str | None = None) -> None:
        self.root = Path(root) if root else Path.cwd()

    def _resolve(self, uri: str) -> Path:
        path = Path(uri)
        if path.is_absolute():
            return path
        return (self.root / path).resolve()

    def exists(self, uri: str) -> bool:
        return self._resolve(uri).exists()

    def read_bytes(self, uri: str) -> bytes:
        return self._resolve(uri).read_bytes()

    def write_bytes(self, uri: str, data: bytes) -> None:
        path = self._resolve(uri)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def write_text(self, uri: str, text: str, encoding: str = "utf-8") -> None:
        self.write_bytes(uri, text.encode(encoding))

    def read_text(self, uri: str, encoding: str = "utf-8") -> str:
        return self.read_bytes(uri).decode(encoding)

    def list(self, prefix: str) -> Iterable[str]:
        base = self._resolve(prefix)
        if not base.exists():
            return []
        if base.is_file():
            return [str(base)]
        return [str(p) for p in sorted(base.rglob("*")) if p.is_file()]

    def join(self, *parts: str) -> str:
        return str(Path(*parts))
