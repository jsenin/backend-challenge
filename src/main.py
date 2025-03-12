from fastapi import FastAPI
import src.settings
import src.mail_client
from src.assistanace_request import AssistanceRequest

app = FastAPI()


@app.post("/request_assistance")
def post(assistance_request: AssistanceRequest):
    mail = src.mail_client.MailClient(src.settings.mail_settings())
    mail.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
              message=assistance_request.description)
    return {"message": "Requested!"}
