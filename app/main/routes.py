from app.main import bp
from app.extensions import API_URL_BASE,headers,get_data,render_template,randrange,sample,Json2Object,Object2Json,session,request,g,redirect,url_for,abort,CURR_USER_KEY,db,jsonify,json,convert_json
from app.models.recipe_favorites import RecipeFavorite

@bp.route('/')
def index():
    url = f"{API_URL_BASE}/recipes/list"

    """get the maximum recipes"""
    data_recipes_random = get_data(url,headers=headers,params={"from":"0","size":"100"})
    """get the maximum dessert recipes"""
    data_recipes_desert = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"desserts"})
    """get the maximum vegetarian recipes"""
    data_recipes_vegetarian = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"vegetarian"})#frank_s_vegetarian_snacks#vegetarian#thanksgiving_vegetarian
    """get the most popular recipes"""
    data_recipes_most_popular = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"christmas"})
    """get the maximum meat lover recipes"""
    data_recipes_meat_lover = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"one_top_app_meat"})#meat_loaf
    """get the maximum gluten free recipes"""
    data_recipes_gluten_free = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"gluten_free"})
    """get the maximum african recipes"""
    data_recipes_african = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"african"}) #african#Jollof Rice

    random_number = randrange(0, len(data_recipes_random.results) - 1)
    random_recipe = data_recipes_random.results[random_number]

    if len(data_recipes_desert.results)>4:
        recipes_desert = sample(data_recipes_desert.results, 4)
    else:
        recipes_desert = sample(data_recipes_desert.results, len(data_recipes_desert.results))

    if len(data_recipes_most_popular.results)>5:
        recipes_most_popular = sample(data_recipes_most_popular.results, 5)
    else:
        recipes_most_popular = sample(data_recipes_most_popular.results, len(data_recipes_most_popular.results))

    if len(data_recipes_meat_lover.results)>5:
        recipes_meat_lover = sample(data_recipes_meat_lover.results, 5)
    else:
        recipes_meat_lover = sample(data_recipes_meat_lover.results, len(data_recipes_meat_lover.results))

    if len(data_recipes_gluten_free.results)>5:
        recipes_gluten_free = sample(data_recipes_gluten_free.results, 5)
    else:
        recipes_gluten_free = sample(data_recipes_gluten_free.results, len(data_recipes_gluten_free.results))

    if len(data_recipes_vegetarian.results)>5:
        recipes_vegetarian = sample(data_recipes_vegetarian.results, 5)
    else:
        recipes_vegetarian = sample(data_recipes_vegetarian.results, len(data_recipes_vegetarian.results))

    if len(data_recipes_african.results)>2:
        recipes_african = sample(data_recipes_african.results, 2)
    else:
        recipes_african = sample(data_recipes_african.results, len(data_recipes_african.results))
    
    return render_template('main/index.html',random_recipe = random_recipe, recipes_desert = recipes_desert,
                           recipes_vegetarian=recipes_vegetarian,recipes_most_popular=recipes_most_popular,
                           recipes_meat_lover=recipes_meat_lover,recipes_gluten_free=recipes_gluten_free,
                           recipes_african=recipes_african)

@bp.route('/recipes/favorites')
def recipes_favorites():
    if CURR_USER_KEY not in session:
                abort(401)

    return render_template('main/favorites.html')


@bp.route('/recipes/pin', methods=["POST"])
def add_pin():
    """Pin and unpin Recipe."""


    """Detail recipe view"""
    if request.method == 'POST':

        data = request.get_data()
        json_object = convert_json(data)
        json_string = json.dumps(json_object)
        final_object = Json2Object(json_string)

        base_data=json_string
        recipe_id=final_object.id
        name=final_object.name
        thumbnail_url=final_object.thumbnail_url
        description=final_object.description
        tag = final_object.tags[0].display_name.replace('_',' ')

        pin = RecipeFavorite.query.filter(RecipeFavorite.user_id==g.user.id,RecipeFavorite.recipe_id==recipe_id).first()

        if pin:
            db.session.delete(pin)
            db.session.commit()

        else:
            pin = RecipeFavorite(user_id=g.user.id,recipe_id=recipe_id,name=name,thumbnail_url=thumbnail_url,description=description,data=base_data,tag=tag)
            db.session.add(pin)
            db.session.commit()

    else:
        abort(401)

    return (jsonify("success"), 201)