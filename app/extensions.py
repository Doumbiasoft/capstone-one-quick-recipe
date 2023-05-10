from flask import Flask, render_template,redirect,flash,url_for,abort,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,TextAreaField,BooleanField
from wtforms.validators import InputRequired,Length
import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()