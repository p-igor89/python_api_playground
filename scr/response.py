import logging
from typing import TypeVar

import allure
from requests import Response


class AssertableResponse:
    T = TypeVar('T', bound='AssertableResponse')

    def __init__(self, response: Response) -> None:
        logging.info("Request: \n url={} \n body={}".format(response.request.url, response.request.body))
        logging.info("Response: \n status={} \n body={}".format(response.status_code, response.text))
        self.response = response

    @allure.step('Response should have {condition}')
    def should_have(self, condition) -> T:
        logging.info('About to check ' + str(condition))
        condition.match(self.response)
        return self
