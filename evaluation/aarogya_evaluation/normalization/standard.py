"""STANDARD normalization — trim, collapse whitespace, Unicode NFKC."""

from __future__ import annotations

import re
import unicodedata


def normalize_standard(text: str) -> str:
    """Trim, NFKC, collapse internal whitespace to single spaces."""
    text = unicodedata.normalize("NFKC", text)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text
