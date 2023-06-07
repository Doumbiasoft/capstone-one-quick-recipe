from app.extensions import render_template,redirect,flash,url_for,abort,request,g,session,jsonify,CURR_USER_KEY,os,APP_STATIC,Send_Email,URLSafeTimedSerializer,SignatureExpired,BadTimeSignature,app_config
from app.auth import bp
from app.forms.auth.login import LoginForm
from app.forms.auth.register import RegisterForm
from app.models.users import User

serializer = URLSafeTimedSerializer(app_config.SECRET_KEY)

@bp.route('/authentication', methods=['GET','POST'])
def authentication():
    """authentication view for user login and sign up"""
    tab_one="active"
    tab_selected_one="true"
    tab_show_one="show"

    tab_two=""
    tab_selected_two="false"
    tab_show_two=""

    if g.user:
        return redirect(url_for('main.index'))

    login_form = LoginForm()
    register_form = RegisterForm()


    if request.method == 'POST' and login_form.validate_on_submit():

        tab_one="active"
        tab_selected_one="true"
        tab_show_one="show"

        tab_two=""
        tab_selected_two="false"
        tab_two=""

        email = login_form.login_email.data
        password = login_form.login_password.data
        user = User.login(email = email.casefold(), password = password)
        if user:
            session[CURR_USER_KEY] = user.id
            login_form.login_email.data=""
            login_form.login_password.data=""
            login_form.login_email.errors =""
            flash('Successfully authenticated!','success')
            return redirect(url_for('main.index'))
        else:
            login_form.login_email.errors = ["Email or Password incorrect!"]
            return render_template('auth/authentication.html',login_form=login_form,register_form=register_form,
                        tab_one=tab_one,
                        tab_selected_one=tab_selected_one,
                        tab_show_one=tab_show_one,
                        tab_two=tab_two,
                        tab_selected_two=tab_selected_two,
                        tab_show_two=tab_show_two,

                        )

    if request.method == 'POST' and register_form.validate_on_submit():

        tab_one=""
        tab_selected_one="false"
        tab_show_one=""

        tab_two="active"
        tab_selected_two="true"
        tab_show_two="show"

        register_first_name = register_form.register_first_name.data
        register_last_name = register_form.register_last_name.data
        register_email = register_form.register_email.data
        register_password = register_form.register_password.data
        register_password_confirm = register_form.register_password_confirm.data

        if register_password == register_password_confirm:

            new_user =  User.register(register_first_name, register_last_name, register_email.casefold(), register_password_confirm,False,False)


            if User.get_users().filter(User.email == register_email, User.is_active==True).count() > 0:
                register_form.register_email.errors = ["This email address already exists. Please enter another one or reset your password!"]
                return render_template('auth/authentication.html',login_form=login_form,register_form=register_form,
                                tab_one=tab_one,
                                tab_selected_one=tab_selected_one,
                                tab_show_one=tab_show_one,
                                tab_two=tab_two,
                                tab_selected_two=tab_selected_two,
                                tab_show_two=tab_show_two,

                                )
            else:
                user = User.get_users().filter(User.email == register_email, User.is_active == False).first()
                if  user:
                    user.first_name = new_user.first_name
                    user.last_name = new_user.last_name
                    user.password = new_user.password
                    if User.update_users(user):
                        send_email_activation(user.first_name,user.email)
                        return redirect(url_for('auth.activation_notification'))

                else:
                    user_save=User.add_users(new_user)
                    if user_save.id:
                        send_email_activation(user_save.first_name,user_save.email)
                        return redirect(url_for('auth.activation_notification'))
        else:
             register_form.register_password_confirm.errors = ["The two passwords entered are not identical!"]
             return render_template('auth/authentication.html',login_form=login_form,register_form=register_form,
                                tab_one=tab_one,
                                tab_selected_one=tab_selected_one,
                                tab_show_one=tab_show_one,
                                tab_two=tab_two,
                                tab_selected_two=tab_selected_two,
                                tab_show_two=tab_show_two,

                                )


    return render_template('auth/authentication.html',login_form=login_form,register_form=register_form,
                           tab_one=tab_one,
                           tab_selected_one=tab_selected_one,
                           tab_show_one=tab_show_one,
                           tab_two=tab_two,
                           tab_selected_two=tab_selected_two,
                           tab_show_two=tab_show_two,

                           )

@bp.route('/logout',methods=['POST'])
def logout():
    if request.method == 'GET':
        abort(401)

    clear_session()
    return (jsonify("success"), 201)


def clear_session():
     if CURR_USER_KEY in session:
         del session[CURR_USER_KEY]

@bp.route('/activation-notification')
def activation_notification():
    if g.user:
        return redirect(url_for('main.index'))
    return render_template('auth/activation_notification_page.html')

@bp.route('/link-expired')
def token_expired_notification():
    if g.user:
        return redirect(url_for('main.index'))
    return render_template('auth/token_expired_page.html')


@bp.route('account-activation/<token>', methods=['GET','POST'])
def account_activation(token):
    if request.method == 'GET':
        try:
            email = serializer.loads(token,max_age=600)
            user = User.get_users().filter(User.email == email, User.is_active == False).first()
            if  user:
                user.is_active = True
                if User.update_users(user):
                    session[CURR_USER_KEY] = user.id
                    send_email_welcome(user.first_name,user.email)
                    flash('Your account has been successfully activated!','success')
                    return redirect(url_for('main.index'))
            else:
             return redirect(url_for('auth.token_expired_notification'))
        except SignatureExpired:
            return redirect(url_for('auth.token_expired_notification'))
        except BadTimeSignature:
             abort(401)
        except Exception:
            return redirect(url_for('auth.token_expired_notification'))
    else:
        abort(401)


def send_email_activation(recipient_name,recipient_email):
    try:

        token = serializer.dumps(recipient_email)
        link = url_for('auth.account_activation',token=token,_external=True)
        subject = "Account Activation"

        with open(os.path.join(APP_STATIC, 'mails/account_activation_template.html')) as f:
            html = f.read()

        msg = html.replace('[FIRST_NAME]',recipient_name)
        msg = msg.replace('[APP_LINK]',url_for('main.index',_external=True))
        msg = msg.replace('[LOGO]',url_for('static',filename='images/quick-recipe-logo.png',_external=True))
        msg = msg.replace('[ILLUS]',url_for('static',filename='images/activation.svg',_external=True))
        msg = msg.replace('[LINK]',link)
        msg = msg.replace('[GITHUB]',url_for('static',filename='images/github.png',_external=True))
        msg = msg.replace('[LINKEDIN]',url_for('static',filename='images/linkedin.png',_external=True))

        Send_Email(recipient_email,subject,msg,'html')
        flash('A notification has been sent to your email address for your account activation please check your email box.!','success')
        return True
    except:
        flash('failed!','danger')
        return False

def send_email_welcome(recipient_name,recipient_email):
    try:

        token = serializer.dumps(recipient_email)
        subject = "Welcome"

        with open(os.path.join(APP_STATIC, 'mails/welcome_template.html')) as f:
            html = f.read()

        msg = html.replace('[FIRST_NAME]',recipient_name)
        msg = msg.replace('[APP_LINK]',url_for('main.index',_external=True))
        msg = msg.replace('[LINK]',url_for('main.index',_external=True))
        msg = msg.replace('[LOGO]',url_for('static',filename='images/quick-recipe-logo.png',_external=True))
        msg = msg.replace('[ILLUS]',url_for('static',filename='images/activation.svg',_external=True))
        msg = msg.replace('[GITHUB]',url_for('static',filename='images/github.png',_external=True))
        msg = msg.replace('[LINKEDIN]',url_for('static',filename='images/linkedin.png',_external=True))

        Send_Email(recipient_email,subject,msg,'html')
        return True
    except:
        flash('failed!','danger')
        return False
