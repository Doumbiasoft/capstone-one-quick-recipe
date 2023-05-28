from app.extensions import FlaskForm,SelectField,StringField

class SearchForm(FlaskForm):
    """Form for searching recipes."""
    recipe = StringField("Search recipe")
    tags = SelectField("Tags",coerce=str)
   