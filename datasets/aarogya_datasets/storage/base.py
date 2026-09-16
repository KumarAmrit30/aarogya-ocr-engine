"""StorageBackend Protocol — local now, S3/GCS/Azure later."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol, runtime_checkable


@runtime_checkable
class StorageBackend(Protocol):
    """Abstract blob/path storage."""

    name: str

    def exists(self, uri: str) -> bool: ...

    def read_bytes(self, uri: str) -> bytes: ...

    def write_bytes(self, uri: str, data: bytes) -> None: ...

    def write_text(self, uri: str, text: str, encoding: str = "utf-8") -> None: ...

    def read_text(self, uri: str, encoding: str = "utf-8") -> str: ...

    def list(self, prefix: str) -> Iterable[str]: ...

    def join(self, *parts: str) -> str: ...
