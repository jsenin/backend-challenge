from fastapi import FastAPI
import src.settings
import src.mail_client

app = FastAPI()


@app.post("/request_assistance")
def post():
    mail = src.mail_client.MailClient(src.settings.mail_settings())
    mail.send(mailto='pricing@fake.com', mail_from='bot@landbot.io', subject='Assistance request',
              message='Need assistance')
    return {"message": "Requested!"}
