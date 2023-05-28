from app.extensions import render_template,redirect,flash,url_for,abort,request,session,API_URL_BASE,headers,get_data
from app.search import bp
from app.forms.search.recipes import SearchForm

url_tags = f"{API_URL_BASE}/tags/list"

@bp.route('/recipes', methods=['GET','POST'])
def recipes():
    """Search view"""

    """get all tags"""
    url_tags = f"{API_URL_BASE}/tags/list"
    data_tags = get_data(url_tags,headers=headers)
    #tags = data_tags.results
    return render_template('search/recipes.html',tags=get_tag_by_type("meal"),list_type=get_type())

@bp.route('/recipes/details', methods=['GET','POST'])
def recipes_details():
    """Detail recipe view"""
    return render_template('search/details.html')

def get_type():
    data_tags = get_data(url_tags,headers=headers)
    tags = data_tags.results
    seen = set()
    unique_list = []
    for obj in tags:
        if obj.type not in seen:
            unique_list.append({"id":f"{obj.type}","name":f"{obj.type.replace('_',' ')}"})
            seen.add(obj.type)
    return unique_list

def get_tag_by_type(type:str):
    data_tags = get_data(url_tags,headers=headers)
    tags = data_tags.results
    seen = set()
    unique_list = []
    for obj in tags:
        if obj.type == type:
            if obj.name not in seen:
               unique_list.append({"id":f"{obj.name}","name":f"{obj.display_name.lower()}"})
               seen.add(obj.name)
    return unique_list
