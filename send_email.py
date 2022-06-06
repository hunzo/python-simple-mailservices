from email.message import EmailMessage

import smtplib


class MailService:
    def __init__(self, username, password, smtp_mail):
        self.username = username
        self.password = password
        self.smtp_mail = smtp_mail

    def send(self, body, subject, recipient):
        smtp_server = smtplib.SMTP(self.smtp_mail, 587)
        msg = EmailMessage()
        msg["Subject"] = subject
        msg.set_content(body, subtype="html")

        smtp_server.set_debuglevel(1)
        smtp_server.starttls()

        smtp_server.login(
            self.username,
            self.password
        )

        smtp_server.sendmail(
            from_addr=self.username,
            to_addrs=recipient,
            msg=msg.as_string())

        smtp_server.close()
