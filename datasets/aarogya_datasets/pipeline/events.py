"""In-process dataset event bus."""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime
from typing import Any

from aarogya_core.types.data_platform import DatasetEvent, DatasetEventType
from aarogya_core.types.ids import DatasetId, VersionId

Handler = Callable[[DatasetEvent], None]


class EventBus:
    """Simple pub/sub — subscribers optional for Phase 3."""

    def __init__(self) -> None:
        self._handlers: dict[DatasetEventType | None, list[Handler]] = {}

    def subscribe(self, event_type: DatasetEventType | None, handler: Handler) -> None:
        self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event: DatasetEvent) -> None:
        for handler in self._handlers.get(event.type, []):
            handler(event)
        for handler in self._handlers.get(None, []):
            handler(event)

    def emit(
        self,
        event_type: DatasetEventType,
        *,
        dataset_id: DatasetId | None = None,
        version_id: VersionId | None = None,
        message: str | None = None,
        payload: dict[str, Any] | None = None,
    ) -> DatasetEvent:
        event = DatasetEvent(
            type=event_type,
            dataset_id=dataset_id,
            version_id=version_id,
            message=message,
            payload=payload or {},
            created_at=datetime.now(UTC),
        )
        self.publish(event)
        return event


default_bus = EventBus()
