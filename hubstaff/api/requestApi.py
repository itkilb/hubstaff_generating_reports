from .auth import Auth
from ..config import Config
import requests


class RequestApi:
    def __init__(self):
        self.access_token = Auth().get_access_token()
        self.base_url = Config.BASE_URL_API_HUBSTAFF

    def _get(self, url, params=None):
        return requests.get(self.base_url + url, params=params, headers={"Authorization": "Bearer " + self.access_token})

    def _post(self, url, params=None):
        return requests.post(self.base_url + url, params=params, headers={"Authorization": "Bearer " + self.access_token})
