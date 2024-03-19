import signal
import mimetypes
from typing import Callable

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, request, Response, send_from_directory


mimetypes.add_type("application/javascript", ".js", True)
APP = Flask(__name__)
APP.config['TEMPLATES_AUTO_RELOAD'] = True
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def handle_request(environ: dict, start_response: Callable):
    return APP(environ, start_response)

@APP.route('/api')
def api_test():
    return 'API'

@APP.route('/api/test')
def api():
    return 'Test route'

@APP.route('/', defaults={'pathvar': ''})
@APP.route('/<path:pathvar>')
def root(pathvar: str):
    if pathvar and "." in pathvar:
        return send_from_directory('static', pathvar)
    else:
        return send_from_directory('static', 'index.html')


def shutdown(server: pywsgi.WSGIServer):
    print("Stopping Server...")
    server.stop()
    server.close()

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 4090), handle_request, handler_class=WebSocketHandler)
    signal.signal(signal.SIGINT, lambda num,info: shutdown(server))
    server.serve_forever()