from app.extensions import FlaskForm,EmailField,Length,PasswordField,InputRequired,StringField

class RegisterForm(FlaskForm):
    """Form for user registration."""

    full_name = StringField("full Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Length(max=50, message='The email must not be longer than 50 characters.')])
    password = PasswordField("Password", validators=[InputRequired()])
    password_confirm = PasswordField("Confirm Password", validators=[InputRequired()])