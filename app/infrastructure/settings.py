import dataclasses

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

def mail_settings():
    return MailSettings(smtp_server='mailpit', smtp_port=1025, username='test', password='password')

def slack_settings():
    return SlackSettings(token='faketoken')


def mail_delivery_settings():
    return MailDeliverySettings(mailto='pricing@landbot.io', mail_from='assistance@landbot.io', subject='Assistance request')


def slack_delivery_settings():
    return SlackDeliverySettings(channel='sales')