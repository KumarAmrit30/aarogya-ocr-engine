"""Dataset API tests."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_datasets_empty_or_ok() -> None:
    response = client.get("/api/v1/datasets")
    assert response.status_code == 200
    assert "datasets" in response.json()


def test_pipeline_run_synthetic(tmp_path: Path, monkeypatch: object) -> None:
    # Point repo root at tmp so we do not mutate real registry
    (tmp_path / "datasets").mkdir()
    (tmp_path / "datasets" / "registry.yaml").write_text(
        "schema_version: '1.0'\ndatasets: []\n", encoding="utf-8"
    )
    (tmp_path / "datasets" / "versions").mkdir()
    (tmp_path / "core").mkdir()
    (tmp_path / "core" / "pyproject.toml").write_text(
        "[project]\nname='x'\n", encoding="utf-8"
    )

    monkeypatch.setenv("AAROGYA_REPO_ROOT", str(tmp_path))  # type: ignore[attr-defined]
    from aarogya_core.config import get_settings

    get_settings.cache_clear() if hasattr(get_settings, "cache_clear") else None  # type: ignore[attr-defined]

    # CoreSettings is not lru_cached — mutate via env + re-instantiate by chdir
    monkeypatch.chdir(tmp_path)  # type: ignore[attr-defined]

    response = client.post(
        "/api/v1/datasets/pipeline/run",
        json={
            "name": "api-synthetic",
            "dataset_id": "DATASET-00001",
            "version": "v1",
            "task": "HTR",
            "domain": "medical",
            "language": ["en"],
            "license": "research-only",
            "tags": ["api"],
        },
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["dataset_id"] == "DATASET-00001"
    assert body["version_id"]
    assert body["fingerprint"]

    listed = client.get("/api/v1/datasets?task=HTR")
    assert listed.status_code == 200
    assert len(listed.json()["datasets"]) >= 1

    detail = client.get(f"/api/v1/datasets/DATASET-00001/versions/{body['version_id']}")
    assert detail.status_code == 200
    assert detail.json()["fingerprint"] == body["fingerprint"]
