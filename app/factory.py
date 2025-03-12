from slack_sdk import WebClient
from app.slack_client import SlackClient

def build_slack_client(token):
    return SlackClient(WebClient(token=token))
