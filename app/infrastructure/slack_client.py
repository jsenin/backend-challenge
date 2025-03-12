from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    def __init__(self, client: WebClient):
        self.client = client

    def send_message(self, channel, message):
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
            return response["ok"]
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return False
