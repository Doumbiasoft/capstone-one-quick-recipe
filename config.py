import os
from email.headerregistry import Address


basedir = os.path.abspath(os.path.dirname(__file__))
database_URI = os.getenv('DATABASE_URL','postgresql:///quick_recipe_db')
if database_URI.startswith("postgres://"):
       database_URI = database_URI.replace("postgres://", "postgresql://", 1)

class Config:
       SECRET_KEY = os.getenv('SECRET_KEY','flask&quick&recipe&secret&key')
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
       API_KEY = os.getenv('API_KEY',None)
       API_CACHE_WEEKS_TIMEOUT = os.getenv('API_CACHE_WEEKS_TIMEOUT',12)
       #--------------send mail parameters-------------
       MAIL_SERVER = os.getenv('MAIL_SERVER','smtp.sendgrid.net')
       MAIL_PORT = os.getenv('MAIL_PORT',465)
       MAIL_SMTP = os.getenv('MAIL_SMTP','smtp.sendgrid.net')
       MAIL_USERNAME = os.getenv('MAIL_USERNAME',None)
       MAIL_PASSWORD = os.getenv('MAIL_PASSWORD',None)
       MAIL_SENDER_NAME = os.getenv('MAIL_SENDER_NAME','Quick Recipe')
       MAIL_SENDER = os.getenv('MAIL_SENDER',None)
       MAIL_DEFAULT_SENDER = Address(display_name = MAIL_SENDER_NAME, addr_spec = MAIL_SENDER)

       #----------Google Oauth2 Authentication parameters --------------------------------

       GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID',None)
       GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID',None)
       GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET',None)
       GOOGLE_REDIRECT_URI_BASE = os.getenv('GOOGLE_REDIRECT_URI_BASE','http://127.0.0.1:5000')

       #----------END Google Oauth2 Authentication parameters --------------------------------

       URL_SAFE_KEY = os.getenv('URL_SAFE_KEY',None)
