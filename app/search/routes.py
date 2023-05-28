from app.extensions import render_template,redirect,flash,url_for,abort,request,session,API_URL_BASE,headers,get_data,sample
from app.search import bp
from app.forms.search.recipes import SearchForm

url = f"{API_URL_BASE}/recipes/list"
url_tags = f"{API_URL_BASE}/tags/list"
data_tags = get_data(url_tags,headers=headers)
tags = data_tags.results


@bp.route('/recipes', methods=['GET','POST'])
def recipes():
    """Search view"""

    querystring = {"from":"0","size":"100"}

    form = SearchForm()
    form.tags.choices = get_tag_tuple()
    if form.validate_on_submit():

        recipe = form.recipe.data
        tag = form.tags.data

        if tag is not None:
            querystring["tags"] = tag.lower()
        if recipe is not None:
            querystring["q"] = recipe.lower()


        data_recipes_found = get_data(url,headers=headers,params=querystring)
        if tag is not None or recipe is not None:
            recipes_found = data_recipes_found.results
        elif tag is None and recipe is None:
            #if len(data_recipes_found.results)>9:
            #   recipes_found = sample(data_recipes_found.results, 9)
            #else:
            #    recipes_found = sample(data_recipes_found.results, len(data_recipes_found.results))
            recipes_found = data_recipes_found.results

        return render_template('search/recipes.html',recipes_found=recipes_found,form=form)

    data_recipes_found = get_data(url,headers=headers,params=querystring)
    #if len(data_recipes_found.results)>9:
    #    recipes_found = sample(data_recipes_found.results, 9)
    #else:
    #   recipes_found = sample(data_recipes_found.results, len(data_recipes_found.results))
    recipes_found = data_recipes_found.results

    return render_template('search/recipes.html',recipes_found=recipes_found,form=form)

@bp.route('/recipes/details', methods=['GET','POST'])
def recipes_details():
    """Detail recipe view"""
    return render_template('search/details.html')

def get_type():
    seen = set()
    unique_list = []
    for obj in tags:
        if obj.type not in seen:
            unique_list.append({"id":f"{obj.type}","name":f"{obj.type.replace('_',' ')}"})
            seen.add(obj.type)
    return unique_list

def get_tag_by_type(type:str):
    seen = set()
    unique_list = []
    for obj in tags:
        if obj.type == type:
            if obj.name not in seen:
               unique_list.append({"id":f"{obj.name}","name":f"{obj.display_name.lower()}"})
               seen.add(obj.name)
    return unique_list

def get_tag():
    seen = set()
    unique_list = []
    for obj in tags:
        if obj.name not in seen:
            unique_list.append({"id":f"{obj.name}","name":f"{obj.display_name.lower()}"})
            seen.add(obj.name)
    return unique_list

def get_tag_tuple():
    seen = set()
    unique_list = []
    unique_list.append(("","-- Tags --"))
    for obj in tags:
        if obj.name not in seen:
            unique_list.append((f"{obj.name}",f"{obj.display_name.lower()}"))
            seen.add(obj.name)
    return unique_list
