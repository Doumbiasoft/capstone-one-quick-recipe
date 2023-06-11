import os
from email.headerregistry import Address


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
       API_KEY = os.environ.get('API_KEY',None)
       API_CACHE_WEEKS_TIMEOUT = os.environ.get('API_CACHE_WEEKS_TIMEOUT',12)
       #--------------send mail parameters-------------
       MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.gmail.com')
       MAIL_PORT = os.environ.get('MAIL_PORT',465)
       MAIL_SMTP = os.environ.get('MAIL_SMTP','smtp.gmail.com')
       MAIL_USERNAME = os.environ.get('MAIL_USERNAME',None)
       MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD',None)
       MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME','Quick Recipe')
       MAIL_DEFAULT_SENDER = Address(display_name = MAIL_SENDER_NAME, addr_spec = MAIL_USERNAME)

       #----------Google Oauth2 Authentication parameters --------------------------------

       GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID',None)
       GOOGLE_PROJECT_ID = os.environ.get('GOOGLE_PROJECT_ID',None)
       GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET',None)
       GOOGLE_REDIRECT_URI_BASE = os.environ.get('GOOGLE_REDIRECT_URI_BASE','http://127.0.0.1:5000')

       #----------END Google Oauth2 Authentication parameters --------------------------------
