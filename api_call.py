import requests
from typing import Optional, Dict
color_love_url = "http://my-json-server.typicode.com/jochman/colors/love"
def get_color_love() -> Optional[Dict]:
    if res := requests.get(color_love_url, verify=False).json():
        return res 
    return None