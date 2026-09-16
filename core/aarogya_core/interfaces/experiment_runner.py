"""Experiment runner interface."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.experiment import Experiment


@runtime_checkable
class ExperimentRunner(Protocol):
    """Orchestrate train/eval for a registered experiment."""

    def run(self, experiment: Experiment) -> Experiment:
        ...
