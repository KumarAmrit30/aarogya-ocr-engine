"""Version and placeholder endpoint tests."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_version() -> None:
    response = client.get("/api/v1/version")
    assert response.status_code == 200
    body = response.json()
    assert body["version"]
    assert body["api_schema_version"] == "1.0"


def test_ocr_not_implemented() -> None:
    response = client.post("/api/v1/ocr", json={"engine_id": "stub"})
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "not_implemented"


def test_train_placeholder() -> None:
    response = client.post("/api/v1/train", json={})
    assert response.status_code == 200
    assert response.json()["status"] == "not_implemented"


def test_evaluate_placeholder() -> None:
    response = client.post("/api/v1/evaluate", json={})
    assert response.status_code == 200
    assert response.json()["status"] == "not_implemented"


def test_models_empty() -> None:
    response = client.get("/api/v1/models")
    assert response.status_code == 200
    assert response.json()["models"] == []
