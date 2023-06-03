from app.extensions import FlaskForm,EmailField,Length,PasswordField,InputRequired,StringField

class RegisterForm(FlaskForm):
    """Form for user registration."""

    register_first_name = StringField("First Name", validators=[InputRequired()])
    register_last_name = StringField("Last Name", validators=[InputRequired()])
    register_email = EmailField("Email", validators=[InputRequired(), Length(max=50, message='The email must not be longer than 50 characters.')])
    register_password = PasswordField("Password", validators=[InputRequired()])
    register_password_confirm = PasswordField("Confirm Password", validators=[InputRequired()])