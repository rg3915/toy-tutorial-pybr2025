from .http import Request, Response, WSGIResponse


class Application:
    def __init__(self):
        self.initialize()

    def initialize(self):
        ...

    def call_handler(self, request: Request) -> Response:
        return Response()

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.call_handler(request)
        wsgi_response = WSGIResponse(response)

        start_response(wsgi_response.status, wsgi_response.header)
        return wsgi_response.body
