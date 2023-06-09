import json
from typing import Final
from requests_cache import CachedSession
from datetime import timedelta
from config import Config
app_config = Config

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace
    
    """Cached session settings"""
requests_cache_session = CachedSession(
    cache_name="app/cache/local_cache",
    expire_after=timedelta(weeks=app_config.API_CACHE_WEEKS_TIMEOUT),    # Otherwise expire responses after three months
    allowable_codes=[200, 400],        # Cache 400 responses as a solemn reminder of your failures
    allowable_methods=['GET', 'POST'], # Cache whatever HTTP methods you want
    ignored_parameters=['api_key','X-RapidAPI-Key']  # Don't match this request param, and redact if from the cache
    )
def convert_json(json_str):
    try:
        json_data = json.loads(json_str, strict=False)
        return json_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {str(e)}")
        return None

def Json2Object(json_text):
    """Convert JSON to a JSON object"""
    return json.loads(json_text, object_hook=lambda d: Namespace(**d))

def Object2Json(obj):
    """Convert a JSON object to JSON text"""
    if isinstance(obj, Namespace):
        obj = vars(obj)
    return json.dumps(obj, default=lambda o: o.__dict__, indent=4)


def get_data(url:str, headers:dict, params:dict=None):
    """Call an API and return a JSON object from the given url and headers and params from cache or api."""
    URL:Final = url
    response = requests_cache_session.get(URL, headers = headers, params = params)
    try:
       data = Json2Object(response.text)
    except Exception as e:
        print(f'{response.status_code} - {e}')
        return None
    return data

