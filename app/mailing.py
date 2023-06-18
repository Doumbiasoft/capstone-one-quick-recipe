import smtplib
import ssl
from email.message import EmailMessage
from config import Config

app_config=Config


def Send_Email(recipient:str,subject:str,message:str,content_type:str="html"):
    
    msg = EmailMessage()
    msg['From'] = app_config.MAIL_DEFAULT_SENDER
    msg['To'] = recipient
    msg['Subject'] = subject
    if content_type =='html':
        msg.set_type('text/html')
        msg.add_alternative(message, subtype="html")
    if content_type =='text':
        msg.set_content(message)

    if str(app_config.MAIL_PORT) == str(465):
        # Add SSL (layer of security)
        context = ssl.create_default_context()
        # Log in and send the email
        with smtplib.SMTP_SSL(app_config.MAIL_SMTP, app_config.MAIL_PORT, context=context) as smtp:
            smtp.login(app_config.MAIL_USERNAME, app_config.MAIL_PASSWORD)
            data = smtp.sendmail(app_config.MAIL_USERNAME, recipient, msg.as_string())

    if str(app_config.MAIL_PORT) == str(587):
        with smtplib.SMTP(app_config.MAIL_SMTP, app_config.MAIL_PORT) as smtp:
            smtp.login(app_config.MAIL_USERNAME, app_config.MAIL_PASSWORD)
            data = smtp.sendmail(app_config.MAIL_USERNAME, recipient, msg.as_string())
        
    return data
    
    
    
    