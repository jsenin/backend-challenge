from app.domain.delivery_strategies.delivery_strategy import DeliveryStrategy
from app.infrastructure import factory
from app.infrastructure.settings import SlackDeliverySettings


class SlackDeliveryStrategy(DeliveryStrategy):
    def __init__(self, settings: SlackDeliverySettings):
        self.settings = settings

    def send(self, message:str):
        slack_client = factory.build_slack_client()
        slack_client.send_message(self.settings.channel, message=message)
