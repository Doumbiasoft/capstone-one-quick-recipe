from app.extensions import render_template,redirect,flash,url_for,abort,request,session
from app.auth import bp
from app.forms.auth.login import LoginForm
from app.forms.auth.register import RegisterForm

@bp.route('/login', methods=['GET','POST'])
def login():
    """login view for user authentication"""
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET','POST'])
def register():
    """register view for user sign up"""
    return render_template('auth/register.html')