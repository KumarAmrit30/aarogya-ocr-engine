"""Structural validation — NOT quality."""

from aarogya_datasets.validators.registry import list_validators
from aarogya_datasets.validators.runner import run_validators

__all__ = ["list_validators", "run_validators"]
