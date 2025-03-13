from fastapi import FastAPI

from app.domain.assistance_request_command import AssistanceRequestCommand
from app.domain.assistance_request_command_handler import AssistanceRequestCommandHandler
from app.domain.delivery_strategies.mail_delivery_strategy import MailDeliveryStrategy
from app.domain.delivery_strategies.slack_delivery_strategy import SlackDeliveryStrategy

fastapi = FastAPI()


@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequestCommand):
    command_handler = AssistanceRequestCommandHandler({'Pricing' : MailDeliveryStrategy(), 'Sales' : SlackDeliveryStrategy()})
    command_handler.handle(assistance_request)
    return {"message": "Requested!"}

