from app.extensions import render_template,redirect,flash,url_for,abort,request,session
from app.auth import bp
from app.forms.auth.login import LoginForm
from app.forms.auth.register import RegisterForm

@bp.route('/authentication', methods=['GET'])
def authentication():
    """authentication view for user login and sign up"""
    return render_template('auth/authentication.html')

@bp.route('/login', methods=['POST'])
def login():
    """login view"""
    return render_template('auth/authentication.html')

@bp.route('/register', methods=['POST'])
def register():
    """register view"""
    return render_template('auth/authentication.html')