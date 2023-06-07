from flask import Flask, render_template,redirect,flash,url_for,abort,request,g,session,jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,TextAreaField,BooleanField,SelectField
from wtforms.validators import InputRequired,Length
import os
import requests
import datetime
from datetime import timedelta
import json
from api_key import api_key
from helpers import Json2Object,get_data,Object2Json,convert_json
from mailing import Send_Email
from random import randrange,sample
import numpy

db = SQLAlchemy()
bcrypt = Bcrypt()

#-------------Admin info-----------
ADMIN_FIRST_NAME='ADMIN_FIRST_NAME'
ADMIN_LAST_NAME='ADMIN_LAST_NAME'
ADMIN_EMAIL='ADMIN_EMAIL'
ADMIN_PASSWORD='ADMIN_PASSWORD'
#---------------end-----------------

RECIPE_ITEM = "recipe_item"
CURR_USER_KEY = "curr_user_key"
API_KEY = os.environ.get('API_KEY',api_key)
API_URL_BASE ="https://tasty.p.rapidapi.com"
headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}
BASE_URI = os.path.dirname(__file__)
# Get absolute path to user's home directory
HOME_DIR = os.path.expanduser('~/')
# '/' is added to ensure the path has a trailing slash
APP_STATIC_DATA_URI = os.path.join(HOME_DIR, '.my_flask_app_app_production/static/')