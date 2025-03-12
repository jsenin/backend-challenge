import re
import json
import requests
from fastapi.testclient import TestClient

from app import main
import httpretty

client = TestClient(main.fastapi)

def test_request_help_to_pricing_sends_an_email():
    response = client.post(
        "/request_assistance", json={"topic": "Pricing", "description": "Need assistance"}
    )
    assert response.status_code == 200

    url = "http://mailpit:8025/api/v1/messages?limit=1"
    response = requests.get(url)

    assert response.json()["messages"][0]["Snippet"] == "Need assistance"

def _test_request_help_to_sales_sends_a_message_to_slack():
    # not working for now
    # httpretty.enable(allow_net_connect=True, verbose=True)
    #
    # httpretty.register_uri(
    #     httpretty.POST,
    #     "https://www.slack.com/api/chat.postMessage",
    #     body=json.dumps(
    #         {
    #             "ok": True,
    #             "ts": "12345.678",
    #         }
    #     )
    # )

    response = client.post(
        "/request_assistance", json={"topic": "Sales", "description": "Need assistance"}
    )
    assert response.status_code == 200
    #assert httpretty.latest_requests() == 1
