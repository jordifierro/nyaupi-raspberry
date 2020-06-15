import os
import smtplib, ssl
from email.message import EmailMessage

port = os.environ['EMAIL_PORT']
smtp_server = os.environ['EMAIL_HOST']
user_email = os.environ['EMAIL_HOST_USER']
password = os.environ['EMAIL_HOST_PASSWORD']
context = ssl.create_default_context()

email_msg = EmailMessage()
email_msg.set_content(os.environ['EMAIL_MESSAGE'])
email_msg['Subject'] = os.environ['EMAIL_SUBJECT']
email_msg['From'] = os.environ['EMAIL_FROM']
email_msg['To'] = os.environ['EMAIL_TO']

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(user_email, password)
    server.send_message(email_msg)
    server.quit()
