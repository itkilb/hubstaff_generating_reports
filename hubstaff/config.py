import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    TOKEN_HUBSTAFF = os.getenv('TOKEN_HUBSTAFF')
    URL_AUTH_HUBSTAFF = "https://account.hubstaff.com/access_tokens"
    BASE_URL_API_HUBSTAFF = "https://api.hubstaff.com/v2/"
    DIR_AUTH_JSON = "auth.json"
    RATE = "500"
