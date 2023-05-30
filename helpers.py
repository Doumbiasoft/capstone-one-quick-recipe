import json
from typing import Final
from requests_cache import CachedSession
from datetime import timedelta

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace
    
    """Cached session settings"""
requests_cache_session = CachedSession(
    cache_name="app/cache/local_cache",
    expire_after=timedelta(weeks=12),    # Otherwise expire responses after one day
    allowable_codes=[200, 400],        # Cache 400 responses as a solemn reminder of your failures
    allowable_methods=['GET', 'POST'], # Cache whatever HTTP methods you want
    ignored_parameters=['api_key','X-RapidAPI-Key']  # Don't match this request param, and redact if from the cache
    )


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

