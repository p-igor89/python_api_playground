import logging


class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request \n url={} \n body={}".format(response.request.url, response.request.body))
        logging.info("Response \n status={} \n body={}".format(response.status_code, response.text))
        self.response = response

    def status_code(self, code):
        logging.info("Assert: status code should be {}".format(code))
        return self.response.status_code == code

    def field(self, name):
        return self.response.json()[name]
