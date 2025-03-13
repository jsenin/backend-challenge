import dataclasses

from fastapi import FastAPI

from app.assistanace_request_command import AssistanceRequestCommand
from app.infrastructure import factory

fastapi = FastAPI()



class DeliveryStrategy:
    def send(self, message: str):
        pass



class AssistanceRequestCommandHandler:
    def __init__(self, delivery_strategies: dict[str, DeliveryStrategy]):
        self.delivery_strategies = delivery_strategies

    def handle(self, assistance_request_command: AssistanceRequestCommand):
        delivery_strategy = self.delivery_strategies[assistance_request_command.topic]
        delivery_strategy.send(message=assistance_request_command.description)

class MailDeliveryStrategy(DeliveryStrategy):
    def send(self, message:str):
        mail_client = factory.build_mail_client()
        mail_client.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
                         message=message)

class SlackDeliveryStrategy(DeliveryStrategy):
    def send(self, message:str):
        slack_client = factory.build_slack_client()
        slack_client.send_message('sales', message=message)

@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequestCommand):
    command_handler = AssistanceRequestCommandHandler({'Pricing' : MailDeliveryStrategy(), 'Sales' : SlackDeliveryStrategy()})
    command_handler.handle(assistance_request)
    return {"message": "Requested!"}

