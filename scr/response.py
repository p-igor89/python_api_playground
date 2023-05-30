class AssertableResponse(object):

    def __init__(self, response):
        self.response = response

    def status_code(self, code):
        return self.response.status_code == code

    def field(self, name):
        return self.response.json()[name]
