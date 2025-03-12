from slack_sdk import WebClient

from app import settings
from app.infrastructure.mail_client import MailClient
from app.infrastructure.slack_client import SlackClient

def build_mail_client():
    return MailClient(settings.mail_settings())

def build_slack_client(token):
    return SlackClient(WebClient(token=token))
