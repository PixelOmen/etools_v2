import mimetypes
from flask import Flask
from typing import Callable

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, request, Response, send_from_directory

mimetypes.add_type("application/javascript", ".js", True)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def handle_request(environ: dict, start_response: Callable):
    return app(environ, start_response)

@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

@app.route('/api')
def api():
    return 'API'

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 4090), handle_request, handler_class=WebSocketHandler)
    server.serve_forever()