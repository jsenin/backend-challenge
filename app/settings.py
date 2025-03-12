import dataclasses

@dataclasses.dataclass
class MailSettings:
    smtp_server: str
    smtp_port: int
    username: str
    password: str


def mail_settings():
    return MailSettings(smtp_server='mailpit', smtp_port=1025, username='test', password='password')