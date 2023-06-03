from flask import Flask, render_template,redirect,flash,url_for,abort,request,g,session,jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,TextAreaField,BooleanField,SelectField
from wtforms.validators import InputRequired,Length
import os
import requests
import datetime
import json
from api_key import api_key
from helpers import Json2Object,get_data,Object2Json,convert_json
from random import randrange,sample
import numpy

db = SQLAlchemy()
bcrypt = Bcrypt()

RECIPE_ITEM = "recipe_item"
CURR_USER_KEY = "curr_user_key"
API_KEY = os.environ.get('API_KEY',api_key)
API_URL_BASE ="https://tasty.p.rapidapi.com"
headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}
