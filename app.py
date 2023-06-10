import smtplib
import imaplib
import re
from email.message import EmailMessage
import email
import csv
from O365 import Account

msg = EmailMessage()

my_address = ""
credentials = ("", "")
account = Account(credentials, tenant_id="")
if account.authenticate(scopes=["basic", "message_all"]):
    print("Authenticated!")  # Let's you know if the authentication was successful

app_generated_password = ""
msg["Subject"] = "The Email Subject"
msg["From"] = my_address
msg["To"] = ""
msg.set_content('Enter Content Here')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_address, app_generated_password)
    print("Sending mail")
    smtp.send_message(msg)
    print("Mail has been sent")
