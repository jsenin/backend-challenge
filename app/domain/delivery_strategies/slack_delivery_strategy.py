from app.domain.delivery_strategies.delivery_strategy import DeliveryStrategy
from app.infrastructure import factory


class SlackDeliveryStrategy(DeliveryStrategy):
    def send(self, message:str):
        slack_client = factory.build_slack_client()
        slack_client.send_message('sales', message=message)
