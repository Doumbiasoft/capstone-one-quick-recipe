from flask import render_template
from app.main import bp
from app.extensions import API_URL_BASE,headers,Json2Object,get_data
from random import randrange,sample

#Jollof Rice
@bp.route('/')
def index():
    url = f"{API_URL_BASE}/recipes/list"
    url_tags = f"{API_URL_BASE}/tags/list"
    data_recipes_random = get_data(url,headers=headers,params={"from":"0","size":"100"})
    data_recipes_desert = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"desserts"})
    data_tags = get_data(url_tags,headers=headers)
    tags = data_tags.results
    #breakpoint()
    random_number = randrange(0, len(data_recipes_random.results) - 1)
    random_recipe = data_recipes_random.results[random_number]
    recipes_desert = sample(data_recipes_desert.results, 4)
    return render_template('index.html',random_recipe = random_recipe, recipes_desert = recipes_desert)

@bp.route('/recipes/favorites')
def recipes_favorites():
    return render_template('favorites.html')