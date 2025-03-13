from app.domain.delivery_strategies.delivery_strategy import DeliveryStrategy
from app.infrastructure import factory


class MailDeliveryStrategy(DeliveryStrategy):
    def send(self, message:str):
        mail_client = factory.build_mail_client()
        mail_client.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
                         message=message)
