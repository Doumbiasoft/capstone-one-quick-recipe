from app.main import bp
from app.extensions import API_URL_BASE,headers,get_data,render_template
from random import randrange,sample

#Jollof Rice
#african#meat_loaf
@bp.route('/')
def index():
    url = f"{API_URL_BASE}/recipes/list"
    url_tags = f"{API_URL_BASE}/tags/list"
    data_recipes_random = get_data(url,headers=headers,params={"from":"0","size":"100"})
    data_recipes_desert = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"desserts"})
    data_tags = get_data(url_tags,headers=headers)
    data_recipes_vegetarian = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"thanksgiving_vegetarian"})
    data_recipes_most_popular = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"christmas"})
    data_recipes_meat_lover = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"one_top_app_meat"})
    data_recipes_gluten_free = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"gluten_free"})
    data_recipes_feature = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"tasty_holiday_festive_favorites"})
    
    tags = data_tags.results
    random_number = randrange(0, len(data_recipes_random.results) - 1)
    random_recipe = data_recipes_random.results[random_number]
    recipes_desert = sample(data_recipes_desert.results, 4)
    
    recipes_vegetarian = sample(data_recipes_vegetarian.results, 4)
    recipes_most_popular = sample(data_recipes_most_popular.results, 5)
    recipes_meat_lover = sample(data_recipes_meat_lover.results, 5)
    recipes_gluten_free = sample(data_recipes_gluten_free.results, 5)
    recipes_feature = sample(data_recipes_feature.results, 2)
    #breakpoint()
    
    return render_template('index.html',random_recipe = random_recipe, recipes_desert = recipes_desert,
                           recipes_vegetarian=recipes_vegetarian,recipes_most_popular=recipes_most_popular,
                           recipes_meat_lover=recipes_meat_lover,recipes_gluten_free=recipes_gluten_free,
                           recipes_feature=recipes_feature)

@bp.route('/recipes/favorites')
def recipes_favorites():
    return render_template('favorites.html')