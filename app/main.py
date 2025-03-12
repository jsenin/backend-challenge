from fastapi import FastAPI

import app.settings
from app.assistanace_request import AssistanceRequest
from app.infrastructure import factory, mail_client

fastapi = FastAPI()


@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequest):
    if assistance_request.topic == 'Pricing':
        mail = mail_client.MailClient(app.settings.mail_settings())
        mail.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
                  message=assistance_request.description)
        return {"message": "Requested!"}

    if assistance_request.topic == 'Sales':
        slack_client = factory.build_slack_client('faketoken')
        slack_client.send_message('sales', assistance_request.description)
        return {"message": "Requested!"}
