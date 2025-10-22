from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
from .application import Application


class HTTPServer:
    def __init__(self, app):
        self.app = app

    def run(self):
        server = WSGIServer(('localhost', 8000), WSGIRequestHandler)
        server.set_app(self.app)

        print('Serving on http://localhost:8000 (press ctrl-c to stop)...')

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nStopping...')


application = Application()

server = HTTPServer(application)
server.run()
