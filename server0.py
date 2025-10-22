from wsgiref.simple_server import WSGIRequestHandler, WSGIServer


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Teste'.encode('utf-8')]


server = WSGIServer(('localhost', 8000), WSGIRequestHandler)
server.set_app(application)
print('Serving on http://localhost:8000 (press ctrl-c to stop)...')
server.serve_forever()
