import json
import os
import allure
import requests

from src.response import AssertableResponse
from typing import Dict


class ApiService:
    def __init__(self) -> None:
        self._base_url: str = os.environ['BASE_URL']

    def _post(self, url: str, body: Dict) -> requests.Response:
        return requests.post(f"{self._base_url}{url}",
                             data=json.dumps(body),
                             headers={'content-type': 'application/json'})


class UserApiService(ApiService):
    def __init__(self) -> None:
        super().__init__()

    @allure.step
    def create_user(self, user: Dict) -> AssertableResponse:
        return AssertableResponse(self._post("/register", user))
