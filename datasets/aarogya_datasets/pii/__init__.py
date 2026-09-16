"""PII metadata helpers — no redaction."""

from aarogya_core.types.data_platform import PIIMetadata, PIIStatus


def default_pii() -> PIIMetadata:
    return PIIMetadata(status=PIIStatus.UNKNOWN)


__all__ = ["PIIMetadata", "PIIStatus", "default_pii"]
