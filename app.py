from fastapi import FastAPI
from pydantic import BaseModel
from send_email import MailService
import os

username = os.environ.get("MAIL_USER", "defaultUser")
password = os.environ.get("MAIL_PASSWORD", "defaultPassword")
smtp_mail = os.environ.get("SMTP", "smtp.office365.com")

app = FastAPI()
mail = MailService(username, password, smtp_mail)


class Payload(BaseModel):
    message: str
    recipient: str
    subject: str


@app.post("/")
def main(payload: Payload):
    body = payload.message
    rcpt = payload.recipient
    subject = payload.subject

    try:
        mail.send(
            body,
            subject,
            rcpt,
        )
        return {
            "success": True
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
