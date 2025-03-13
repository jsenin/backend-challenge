from app.domain.delivery_strategies.delivery_strategy import DeliveryStrategy
from app.infrastructure import factory
from app.infrastructure.settings import MailDeliverySettings


class MailDeliveryStrategy(DeliveryStrategy):
    def __init__(self, settings: MailDeliverySettings):
        self.settings = settings

    def send(self, message:str):
        mail_client = factory.build_mail_client()
        mail_client.send(mailto=self.settings.mailto, mail_from=self.settings.mail_from, subject=self.settings.subject,
                         message=message)
