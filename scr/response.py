import logging
import allure
from requests import Response
from typing import TypeVar


class AssertableResponse:
    T = TypeVar('T', bound='AssertableResponse')

    def __init__(self, response: Response) -> None:
        logging.info(f"Request:\nurl={response.request.url}\nbody={response.request.body}")
        logging.info(f"Response:\nstatus={response.status_code}\nbody={response.text}")
        self.response = response

    @allure.step('Response should have {condition}')
    def should_have(self, condition) -> T:
        logging.info('About to check ' + str(condition))
        condition.match(self.response)
        return self
