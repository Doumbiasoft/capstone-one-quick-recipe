from app.extensions import FlaskForm,EmailField,Length,PasswordField,InputRequired

class LoginForm(FlaskForm):
    """Form for user authentication."""
    email = EmailField("Email", validators=[InputRequired(), Length(max=50, message='The email must not be longer than 50 characters.')])
    password = PasswordField("Password", validators=[InputRequired()])
   