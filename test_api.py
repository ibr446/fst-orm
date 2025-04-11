from http.client import responses

from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_read_main():
    response = client.get("/api/user")
    assert response.status_code == 200