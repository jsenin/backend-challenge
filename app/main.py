from fastapi import FastAPI

from app.assistanace_request import AssistanceRequest
from app.infrastructure import factory

fastapi = FastAPI()
class AssistanceRequestByMail:
    @staticmethod
    def send(message:str):
        mail_client = factory.build_mail_client()
        mail_client.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
                         message=message)

class AssistanceRequestBySlack:
    @staticmethod
    def send(message:str):
        slack_client = factory.build_slack_client()
        slack_client.send_message('sales', message=message)

@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequest):
    if assistance_request.topic == 'Pricing':
        AssistanceRequestByMail.send(assistance_request.description)
        return {"message": "Requested!"}

    if assistance_request.topic == 'Sales':
        AssistanceRequestBySlack.send(assistance_request.description)
        return {"message": "Requested!"}
