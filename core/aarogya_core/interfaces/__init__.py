"""Replaceable component Protocols for the Research Core."""

from aarogya_core.interfaces.benchmark_runner import BenchmarkRunner
from aarogya_core.interfaces.checkpoint_manager import CheckpointManager
from aarogya_core.interfaces.dataset_loader import DatasetLoader
from aarogya_core.interfaces.detector import Detector
from aarogya_core.interfaces.evaluation_runner import EvaluationRunner
from aarogya_core.interfaces.evaluator import Evaluator
from aarogya_core.interfaces.experiment_runner import ExperimentRunner
from aarogya_core.interfaces.inference_engine import InferenceEngine
from aarogya_core.interfaces.layout import LayoutAnalyzer
from aarogya_core.interfaces.medical_parser import MedicalParser
from aarogya_core.interfaces.metrics_calculator import MetricsCalculator
from aarogya_core.interfaces.model_registry import ModelRegistry
from aarogya_core.interfaces.pipeline import Pipeline
from aarogya_core.interfaces.postprocessor import Postprocessor
from aarogya_core.interfaces.preprocessor import Preprocessor
from aarogya_core.interfaces.reading_order import ReadingOrder
from aarogya_core.interfaces.recognizer import Recognizer
from aarogya_core.interfaces.table import TableExtractor
from aarogya_core.interfaces.training_runner import TrainingRunner
from aarogya_core.interfaces.vlm import VisionLanguageModel

__all__ = [
    "Detector",
    "Recognizer",
    "Preprocessor",
    "Postprocessor",
    "LayoutAnalyzer",
    "TableExtractor",
    "ReadingOrder",
    "VisionLanguageModel",
    "MedicalParser",
    "Pipeline",
    "Evaluator",
    "DatasetLoader",
    "TrainingRunner",
    "EvaluationRunner",
    "ExperimentRunner",
    "MetricsCalculator",
    "InferenceEngine",
    "CheckpointManager",
    "ModelRegistry",
    "BenchmarkRunner",
]
