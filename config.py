import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_URI = os.environ.get('DATABASE_URL','postgresql:///quick_recipe_db')
if database_URI.startswith("postgres://"):
       database_URI = database_URI.replace("postgres://", "postgresql://", 1)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','flask&quick&recipe&secret&key')
    SQLALCHEMY_DATABASE_URI = database_URI\
    or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECT = False
    TESTING = True
    DEBUG_TB_HOSTS = ['dont-show-debug-toolbar']
    #WTF_CSRF_ENABLED = False
