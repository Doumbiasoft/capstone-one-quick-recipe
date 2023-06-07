import os
import smtplib
import ssl
from email.message import EmailMessage
from email.headerregistry import Address
from api_key import email_key,email_sender,email_sender_name

MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.gmail.com') 
MAIL_PORT = os.environ.get('MAIL_PORT',465)
MAIL_SMTP = os.environ.get('MAIL_SMTP','smtp.gmail.com')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME',email_sender)
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD',email_key) 
MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME',email_sender_name) 
MAIL_DEFAULT_SENDER = Address(display_name = MAIL_SENDER_NAME, addr_spec = MAIL_USERNAME)


def Send_Email(recipient:str,subject:str,message:str,content_type:str="html"):
    
    msg = EmailMessage()
    msg['From'] = MAIL_DEFAULT_SENDER 
    msg['To'] = recipient
    msg['Subject'] = subject
    if content_type =='html':
        msg.set_type('text/html')
        msg.add_alternative(message, subtype="html")
    if content_type =='text':
        msg.set_content(message)
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send the email
    with smtplib.SMTP_SSL(MAIL_SMTP, MAIL_PORT, context=context) as smtp:
        smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
        data = smtp.sendmail(MAIL_USERNAME, recipient, msg.as_string())
        
    return data
    
    
    
    