"""Append-only sample provenance store."""

from __future__ import annotations

from aarogya_core.errors import RegistryError
from aarogya_core.types.data_platform import SampleProvenance
from aarogya_datasets.storage.local import LocalStorage


class ProvenanceStore:
    def __init__(self, storage: LocalStorage, root_uri: str) -> None:
        self.storage = storage
        self.root_uri = root_uri

    def _path(self, sample_id: str) -> str:
        return self.storage.join(self.root_uri, f"{sample_id}.json")

    def write(self, record: SampleProvenance, *, overwrite: bool = False) -> str:
        uri = self._path(str(record.sample_id))
        if self.storage.exists(uri) and not overwrite:
            raise RegistryError(
                f"Provenance for {record.sample_id} already exists (immutable)"
            )
        self.storage.write_text(uri, record.model_dump_json(indent=2))
        return uri

    def get(self, sample_id: str) -> SampleProvenance | None:
        uri = self._path(sample_id)
        if not self.storage.exists(uri):
            return None
        return SampleProvenance.model_validate_json(self.storage.read_text(uri))
