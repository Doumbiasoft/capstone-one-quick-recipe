from app.main import bp
from app.extensions import API_URL_BASE,headers,get_data,render_template,randrange,sample,Json2Object,Object2Json,session,request,g,redirect,url_for,abort,CURR_USER_KEY,db,jsonify,json,convert_json,flash,Send_Email,os,APP_STATIC
from app.models.recipe_favorites import RecipeFavorite
from app.models.users import User



@bp.route('/')
def index():
    url = f"{API_URL_BASE}/recipes/list"

    """get the maximum recipes"""
    data_recipes_random = get_data(url,headers=headers,params={"from":"0","size":"100","approved_at":"asc"})
    """get the maximum dessert recipes"""
    data_recipes_desert = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"desserts","approved_at":"asc"})
    """get the maximum vegetarian recipes"""
    data_recipes_vegetarian = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"vegetarian","approved_at":"asc"})
    """get the most popular recipes"""
    data_recipes_most_popular = data_recipes_random
    """get the maximum meat lover recipes"""
    data_recipes_meat_lover = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"one_top_app_meat","approved_at":"asc"})
    """get the maximum gluten free recipes"""
    data_recipes_gluten_free = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"gluten_free","approved_at":"asc"})
    """get the maximum african recipes"""
    data_recipes_african = get_data(url,headers=headers,params={"from":"0","size":"100","tags":"african","approved_at":"asc"})

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
    if not g.user:
        return redirect(url_for('main.index'))

    return render_template('main/favorites.html')

@bp.route('/subscribers')
def get_subscribers():
    if CURR_USER_KEY in session and g.user:
       if not g.user.is_admin:
          abort(401)
       else:
          list_subscribers = User.query.filter(User.is_admin == False)
    else:
         return redirect(url_for('auth.authentication'))

    return render_template('main/subscribers.html',list_subscribers=list_subscribers)

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

@bp.route('/user/profile')
def user_profile():
    if not g.user:
        return redirect(url_for('auth.authentication'))


    return render_template('main/profile.html')

@bp.route('/user/edit-info',methods=['POST'])
def user_edit_info():
    if g.user:
       if request.method == 'POST':
           data = Json2Object(request.get_data())
           first_name = data.first_name
           last_name = data.last_name
           user = User.query.filter(User.id==g.user.id).first()
           if user:
               user.first_name = first_name
               user.last_name = last_name
               db.session.add(user)
               db.session.commit()
               return (jsonify("success"), 201)
           else:
               return (jsonify("failed"),300)

@bp.route('/user/check-current-pass',methods=['POST'])
def user_check_current_pass():

    if g.user:
       if request.method == 'POST':
           data = Json2Object(request.get_data())
           password = data.curr_password

           if User.hash_function_check(g.user.password,password):
               return (jsonify("success"), 201)
           else:
               return (jsonify("failed"),201)

@bp.route('/user/save-password',methods=['POST'])
def user_save_password():
    if g.user:
       if request.method == 'POST':
           data = Json2Object(request.get_data())
           new_password = data.new_password
           user = User.query.filter(User.id==g.user.id).first()
           if user:
               user.password = User.hash_function(new_password)
               db.session.add(user)
               db.session.commit()
               return (jsonify("success"), 201)
           else:
               return (jsonify("failed"),300)

@bp.route('/user/delete-account',methods=['POST'])
def user_delete_account():
    if g.user:
       if request.method == 'POST':
           data = Json2Object(request.get_data())
           email = data.email
           user = User.query.filter(User.id==g.user.id).first()
           if user and user.email==email:
               db.session.delete(user)
               db.session.commit()
               if CURR_USER_KEY in session:
                  del session[CURR_USER_KEY]
                  flash('Account deleted Successfully!','success')
               return (jsonify("success"), 201)
           else:
               return (jsonify("failed"),300)
