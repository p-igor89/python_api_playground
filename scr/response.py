import logging
import allure


class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request: \n url={} \n body={}".format(response.request.url, response.request.body))
        logging.info("Response: \n status={} \n body={}".format(response.status_code, response.text))
        self.response = response

    @allure.step('Response should have {condition}')
    def should_have(self, condition):
        logging.info('About to check ' + str(condition))
        condition.match(self.response)
        return self
