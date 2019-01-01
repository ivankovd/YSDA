import random
import urllib.parse

from utils import config
import keys

import requests


class PicFinder:
    def __init__(self):
        self.headers = {
            'Ocp-Apim-Subscription-Key': keys.BING_KEY
        }

        self.params_template = {
            'q': None,
            'count': '10',
            'offset': '0',
            'mkt': "en-us",
            'safeSearch': 'Moderate'
        }

    def get_pic(self, query):
        self.params_template["q"] = query
        params = urllib.parse.urlencode(self.params_template)

        req = requests.get(
            url=config.SEARCH_PIC_PAGE,
            params=params, headers=self.headers)

        url = self._get_url(req.json())
        return {"url": url}

    def _get_url(self, server_response):
        try:
            m = min(7, len(server_response["value"]) - 1)
            url = server_response["value"][random.randint(0, m)][
                "thumbnailUrl"]
            return url

        except Exception:
            return None


if __name__ == '__main__':
    pic_finder = PicFinder()
    url = pic_finder.get_pic("moscow cloudy")
    print(url)
