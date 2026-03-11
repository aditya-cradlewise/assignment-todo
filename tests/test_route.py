import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_list_api(client):
    response = client.post("/lists", json={"title": "API List"})
    assert response.status_code == 201
    assert "id" in response.json