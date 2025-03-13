import configparser
import dataclasses
import os


@dataclasses.dataclass
class MailSettings:
    smtp_server: str
    smtp_port: int
    username: str
    password: str


@dataclasses.dataclass
class SlackSettings:
    token: str

@dataclasses.dataclass
class MailDeliverySettings:
    mailto:str
    mail_from: str
    subject: str

@dataclasses.dataclass
class SlackDeliverySettings:
    channel:str


config_file = os.path.dirname(__file__) + "/../../config/config.ini"
config = configparser.ConfigParser()
config.read(config_file)


def mail_settings():
    smtp_server = os.getenv("MAIL_HOST") or config["MAIL"]["host"]
    smtp_port = os.getenv("MAIL_PORT") or config["MAIL"]["port"]
    username = os.getenv("MAIL_USER") or config["MAIL"]["user"]
    password = os.getenv("MAIL_PASSWORD") or config["MAIL"]["password"]

    return MailSettings(smtp_server=smtp_server, smtp_port=int(smtp_port), username=username, password=password)

def slack_settings():
    api_token = os.getenv("SLACK_API_TOKEN") or config["SLACK"]["api_token"]
    return SlackSettings(token=api_token)


def mail_delivery_settings():
    mailto = config["PRICING"]["mailto"]
    mail_from = config["PRICING"]["mail_from"]
    subject = config["PRICING"]["subject"]
    return MailDeliverySettings(mailto=mailto, mail_from=mail_from, subject=subject)


def slack_delivery_settings():
    slack_channel = config["SALES"]["slack_channel"]
    return SlackDeliverySettings(channel=slack_channel)