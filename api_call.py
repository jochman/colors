import requests
from typing import Dict, Optional

class GetColors:
    @classmethod
    def loved_colors(cls) -> Optional[Dict]:
        color_love_url = "http://my-json-server.typicode.com/jochman/colors/love"
        if res := requests.get(color_love_url, verify=False).json():
            return res
        return None

    @classmethod
    def hated_colors(cls)-> Optional[Dict]:
        color_love_url = "http://my-json-server.typicode.com/jochman/colors/hate"
        if res := requests.get(color_love_url, verify=False).json():
            return res
        return None
