import json

import requests


class ApiService(object):

    def __init__(self):
        pass


class UserApiService(ApiService):

    def __init__(self):
        super.__init__()

    @staticmethod
    def create_user(user: dict) -> requests.Response:
        return requests.post('http://0.0.0.0/register',
                             data=json.dumps(user),
                             headers={'content-type': 'application/json'})
