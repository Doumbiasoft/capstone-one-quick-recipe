from app.extensions import render_template,redirect,flash,url_for,abort,request,g,session,jsonify,CURR_USER_KEY
from app.auth import bp
from app.forms.auth.login import LoginForm
from app.forms.auth.register import RegisterForm
from app.models.users import User




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

            new_user =  User.register(register_first_name, register_last_name, register_email.casefold(), register_password_confirm,False)

            if User.get_users().filter(User.email == register_email).count() > 0:
                register_form.register_email.errors = ["This email address already exists. Please enter another one!"]
                return render_template('auth/authentication.html',login_form=login_form,register_form=register_form,
                                tab_one=tab_one,
                                tab_selected_one=tab_selected_one,
                                tab_show_one=tab_show_one,
                                tab_two=tab_two,
                                tab_selected_two=tab_selected_two,
                                tab_show_two=tab_show_two,

                                )
            else:
                User.add_users(new_user)
                if new_user.id:
                    session[CURR_USER_KEY] = new_user.id
                    flash('Account created successfully!','success')
                    return redirect(url_for('main.index'))
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