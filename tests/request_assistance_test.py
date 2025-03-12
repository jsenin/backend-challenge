import requests
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.fastapi)

def test_request_help_to_pricing_sends_an_email():
    response = client.post(
        "/request_assistance", json={"topic": "Pricing", "description": "Need assistance"}
    )
    assert response.status_code == 200

    url = "http://mailpit:8025/api/v1/messages?limit=1"
    response = requests.get(url)

    assert response.json()["messages"][0]["Snippet"] == "Need assistance"
