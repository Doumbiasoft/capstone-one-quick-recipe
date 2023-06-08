import os
from email.headerregistry import Address
from api_key import api_key,email_key,email_sender,email_sender_name


basedir = os.path.abspath(os.path.dirname(__file__))
database_URI = os.environ.get('DATABASE_URL','postgresql:///quick_recipe_db')
if database_URI.startswith("postgres://"):
       database_URI = database_URI.replace("postgres://", "postgresql://", 1)

class Config:
       SECRET_KEY = os.environ.get('SECRET_KEY','flask&quick&recipe&secret&key')
       SESSION_TYPE = 'filesystem'
       SQLALCHEMY_DATABASE_URI = database_URI\
       or 'sqlite:///' + os.path.join(basedir, 'app.db')
       SQLALCHEMY_TRACK_MODIFICATIONS = False
       SQLALCHEMY_ECHO = True
       DEBUG_TB_INTERCEPT_REDIRECT = False
       TESTING = True
       DEBUG_TB_HOSTS = ['dont-show-debug-toolbar']
       #WTF_CSRF_ENABLED = False
       #--------------food Api Key-------------
       API_KEY = os.environ.get('API_KEY',api_key)
       #--------------send mail parameters-------------
       MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.gmail.com')
       MAIL_PORT = os.environ.get('MAIL_PORT',465)
       MAIL_SMTP = os.environ.get('MAIL_SMTP','smtp.gmail.com')
       MAIL_USERNAME = os.environ.get('MAIL_USERNAME',email_sender)
       MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD',email_key)
       MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME',email_sender_name)
       MAIL_DEFAULT_SENDER = Address(display_name = MAIL_SENDER_NAME, addr_spec = MAIL_USERNAME)
