from main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_get_user():
    response = client.get("/user")
    assert response.status_code == 405
    assert response.json()







