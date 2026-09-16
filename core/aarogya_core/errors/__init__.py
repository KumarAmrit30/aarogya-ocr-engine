"""Shared exception hierarchy."""


class AarogyaError(Exception):
    """Base error for the research platform."""


class NotImplementedComponentError(AarogyaError):
    """Raised when a stub component is invoked before implementation."""


class RegistryError(AarogyaError):
    """Raised for registry load / ID / validation failures."""


class ConfigError(AarogyaError):
    """Raised for config load or validation failures."""
