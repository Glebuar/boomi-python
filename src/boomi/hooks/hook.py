

class Request:
    def __init__(self, method, url, headers, body=""):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return "Response(status={}, headers={}, body={})".format(
            self.status, self.headers, self.body
        )


class DefaultHook:

    def before_request(self, request: Request, **kwargs):
        pass

    def after_response(self, request: Request, response: Response, **kwargs):
        pass

    def on_error(
        self, error: Exception, request: Request, response: Response, **kwargs
    ):
        pass
