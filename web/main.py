from fastapi import FastAPI

from app.domain.assistance_request_command import AssistanceRequestCommand
from app.domain.assistance_request_command_handler import AssistanceRequestCommandHandler
from app.infrastructure.delivery_strategies import factory

fastapi = FastAPI()


@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequestCommand):
    command_handler = AssistanceRequestCommandHandler(factory.build_delivery_strategies())
    command_handler.handle(assistance_request)
    return {"message": "Requested!"}

