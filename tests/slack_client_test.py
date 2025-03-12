from slack_sdk import WebClient
from unittest.mock import MagicMock, patch, Mock

from app import factory
from app.slack_client import SlackClient


def test_send_message_to_slack():

    mock_client = Mock()
    mock_client.chat_postMessage = MagicMock(return_value={"ok": True})
    slack = SlackClient(client=mock_client)

    status = slack.send_message("#test-channel", "Hello, Slack!")

    assert status is True
