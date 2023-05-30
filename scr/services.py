import json

import requests

from scr.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        pass

    def _post(self, url, body):
        return requests.post(f"http://0.0.0.0{url}",
                             data=json.dumps(body),
                             headers={'content-type': 'application/json'})


class UserApiService(ApiService):

    def __init__(self) -> None:
        super().__init__()

    def create_user(self, user: dict):
        return AssertableResponse(self._post("/register", user))
