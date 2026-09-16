"""Small shared utilities."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any


def sha256_file(path: Path, chunk_size: int = 65536) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def config_hash(payload: dict[str, Any] | str) -> str:
    if isinstance(payload, dict):
        import json

        text = json.dumps(payload, sort_keys=True, default=str)
    else:
        text = payload
    return sha256_text(text)[:16]
