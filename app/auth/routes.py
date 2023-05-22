from app.extensions import render_template,redirect,flash,url_for,abort,request,session
from app.auth import bp
from app.forms.auth.login import LoginForm
from app.forms.auth.register import RegisterForm

@bp.route('/authentication', methods=['GET','POST'])
def authentication():
    """register view for user login and sign up"""
    return render_template('auth/authentication.html')