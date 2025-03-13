from app.domain.assistance_request_command import AssistanceRequestCommand
from app.domain.delivery_strategies.delivery_strategy import DeliveryStrategy


class AssistanceRequestCommandHandler:
    def __init__(self, delivery_strategies: dict[str, DeliveryStrategy]):
        self.delivery_strategies = delivery_strategies

    def handle(self, assistance_request_command: AssistanceRequestCommand):
        delivery_strategy = self.delivery_strategies[assistance_request_command.topic]
        delivery_strategy.send(message=assistance_request_command.description)