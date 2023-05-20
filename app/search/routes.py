from app.extensions import render_template,redirect,flash,url_for,abort,request,session
from app.search import bp
from app.forms.search.recipes import SearchForm

@bp.route('/recipes', methods=['GET','POST'])
def recipes():
    """Search view"""
    return render_template('search/recipes.html')

@bp.route('/recipes/details', methods=['GET','POST'])
def recipes_details():
    """Detail recipe view"""
    return render_template('search/details.html')