from ..config import Config
import requests
import json
import os.path


class Auth:
    def __init__(self):
        self.refresh_token = Config.TOKEN_HUBSTAFF
        self.url_auth_hubstaff = Config.URL_AUTH_HUBSTAFF
        self.base_url_api = Config.BASE_URL_API_HUBSTAFF
        self.auth_file = Config.DIR_AUTH_JSON

    def get_access_token(self):
        if os.path.exists(self.auth_file):
            self.__read_token_file()
            if self.__check_token():
                return self.access_token
        self.__request_access_token()
        self.__save_token_file()
        return self.access_token

    def __save_token_file(self):
        with open(self.auth_file, 'w') as fp:
            json.dump({'access_token': self.access_token}, fp)

    def __read_token_file(self):
        with open(self.auth_file, 'r') as f:
            self.access_token = json.load(f)['access_token']

    def __check_token(self):
        status_code = requests.get(self.base_url_api + '/users/me',
                                   headers={"Authorization": "Bearer " + self.access_token}).status_code
        if status_code == 200:
            return True
        else:
            return False

    def __request_access_token(self):
        self.access_token = \
            requests.post(self.url_auth_hubstaff, params={'grant_type': 'refresh_token', 'refresh_token': \
                self.refresh_token}).json()['access_token']
