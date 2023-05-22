from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recipes/favorites')
def recipes_favorites():
    return render_template('favorites.html')
