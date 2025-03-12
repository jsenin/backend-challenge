from fastapi.testclient import TestClient

from src import main

client = TestClient(main.app)


def test_request_help_to_sales_returns_200():
    response = client.post(
        "/request_assistance", json={"topic": "Sales", "description": "Need assistance"}
    )
    assert response.status_code == 200
