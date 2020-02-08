class Response:
    def __init__(self):
        self.status_code = 400
        self.message = None
        self.data = None
        self.errors = None

    def to_dict(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
            'data': self.data,
            'errors': self.errors
        }
