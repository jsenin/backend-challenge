from fastapi import FastAPI

import app.settings
import app.mail_client
from app.assistanace_request import AssistanceRequest

fastapi = FastAPI()


@fastapi.post("/request_assistance")
def post(assistance_request: AssistanceRequest):
    mail = app.mail_client.MailClient(app.settings.mail_settings())
    mail.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
              message=assistance_request.description)
    return {"message": "Requested!"}
