import abc
import jsonpath_rw
from hamcrest import assert_that
from requests import Response
from typing import Any


class Condition(abc.ABC):

    @abc.abstractmethod
    def match(self, response: Response) -> None:
        pass


class StatusCodeCondition(Condition):

    def __init__(self, code: int) -> None:
        super().__init__()
        self._status_code: int = code

    def __repr__(self) -> str:
        return f"Status code is {self._status_code}"

    def match(self, response: Response) -> None:
        assert response.status_code == self._status_code


status_code = StatusCodeCondition


class BodyFieldCondition(Condition):

    def __init__(self, json_path: str, matcher: Any) -> None:
        super().__init__()
        self._json_path: str = json_path
        self._matcher: Any = matcher

    def __repr__(self) -> str:
        return f"Body field is {self._json_path} {self._matcher}"

    def match(self, response: Response) -> None:
        json_data = response.json()
        value = jsonpath_rw.parse(self._json_path).find(json_data)
        assert_that(value, self._matcher)


body = BodyFieldCondition
