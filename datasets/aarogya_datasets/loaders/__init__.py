"""Dataset loaders — import registers stubs."""

from aarogya_datasets.loaders import (  # noqa: F401
    custom,
    doclaynet,
    iam,
    m5hisdoc,
    rxhandbd,
    synthdog,
    synthetic,
)
from aarogya_datasets.loaders.registry import get_loader, list_loaders

__all__ = ["get_loader", "list_loaders"]
