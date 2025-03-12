import smtplib

from src.settings import MailSettings

class MailClient:
    def __init__(self, settings: MailSettings):
        self.settings = settings

    def send(self, mailto: str, mail_from: str, subject: str, message: str) -> None:
        port = self.settings.smtp_port
        smtp_server = self.settings.smtp_server
        username = self.settings.username
        password = self.settings.password
        message = f"""\
        Subject: {subject}

        {message}"""

        # context = ssl.create_default_context()
        # context = ssl._create_unverified_context()
        with smtplib.SMTP(smtp_server, port) as server:
            # server.ehlo()
            # server.starttls(context=context)
            # server.ehlo()
            # server.login(username, password)
            server.sendmail(mail_from, mailto, message)
