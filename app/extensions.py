from flask import Flask, render_template,redirect,flash,url_for,abort,request,g,session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,TextAreaField,BooleanField
from wtforms.validators import InputRequired,Length
import os
import requests
import datetime
from api_key import api_key
from helpers import Json2Object,get_data



db = SQLAlchemy()
bcrypt = Bcrypt()

CURR_USER_KEY = "curr_user"
CURR_USER_FULLNAME = "curr_user_fullname"
CURR_USER_IS_ADMIN = "curr_user_is_admin"
API_KEY = os.environ.get('API_KEY',api_key)
API_URL_BASE ="https://tasty.p.rapidapi.com"
headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}
