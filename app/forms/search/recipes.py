from app.extensions import FlaskForm,EmailField,Length,PasswordField,InputRequired

class SearchForm(FlaskForm):
    """Form for searching recipes."""
    email = EmailField("Email", validators=[InputRequired(), Length(max=50, message='The email must not be longer than 50 characters.')])
    password = PasswordField("Password", validators=[InputRequired()])
   