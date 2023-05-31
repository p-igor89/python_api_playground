import json
import os
import allure
import requests

from scr.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self._base_url = os.environ['BASE_URL']

    def _post(self, url, body):
        return requests.post(f"{self._base_url}" + url,
                             data=json.dumps(body),
                             headers={'content-type': 'application/json'})


class UserApiService(ApiService):

    def __init__(self) -> None:
        super().__init__()

    @allure.step
    def create_user(self, user: dict):
        return AssertableResponse(self._post("/register", user))
