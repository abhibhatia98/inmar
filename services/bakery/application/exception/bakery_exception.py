from shared.application.error.error_message import ErrorMessage


class BakeryException(Exception):
    def __init__(self, message: str, status_code=None, payload=None):
        super(BakeryException, self).__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
