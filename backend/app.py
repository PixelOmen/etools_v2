import uuid
import signal
import mimetypes
from typing import Callable
from datetime import datetime
from collections import deque

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, request, Response, send_from_directory, session

from libs import dcpomatic
from libs.navlib import navlinks
from libs.config import get_config

CONFIG = get_config()
dcpomatic.set_config(CONFIG)

mimetypes.add_type("application/javascript", ".js", True)
APP = Flask(__name__)
APP.config['TEMPLATES_AUTO_RELOAD'] = True
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
APP.secret_key = str(uuid.uuid4())


def log_request(remoteip: str, msg: str) -> None:
    now = datetime.now()
    timeheader = now.strftime("[%d/%b/%Y %H:%M:%S]")
    addrheader = f"{remoteip} - - "
    print(f"{addrheader+timeheader} \"{msg}\"")

def handle_request(environ: dict, start_response: Callable):
    return APP(environ, start_response)

@APP.route('/api/nav')
def nav():
    return navlinks()

@APP.route('/api/certs')
def certs():
    return dcpomatic.get_certs(CONFIG.certdir)

@APP.route('/api/dkdms')
def dkdms():
    return dcpomatic.get_dkdms(CONFIG.dkdmdir)

@APP.route("/api/kdm/history")
def kdmhistory():
    if "history" in session:
        return session['history']
    return []

@APP.route('/api/kdm/submit', methods=["POST"])
def submit():
    if request.method != "POST":
        return Response(status=400)

    if 'lastid' in session:
        jobid = str(int(session['lastid']) + 1)
    else:
        jobid = "0"
        session.permanent = True
        session['history'] = []

    session['lastid'] = jobid

    try:
        jdict = request.json
    except Exception as e:
        return {"status": "error", "error": str(e)}
    
    log_request(request.remote_addr, "KDM Request") #type:ignore
    kdmsessions = dcpomatic.process_request(jdict, jobid)

    session_q = deque(maxlen=100)
    session_q.extend(session['history'])
    session_q.extend([sess.as_dict() for sess in kdmsessions])
    session['history'] = list(session_q)
    return Response(status=200)

@APP.route('/', defaults={'pathvar': ''})
@APP.route('/<path:pathvar>')
def root(pathvar: str):
    if pathvar and "." in pathvar:
        return send_from_directory('static', pathvar)
    else:
        return send_from_directory('static', 'index.html')


def shutdown(server: pywsgi.WSGIServer) -> None:
    print("Stopping Server...")
    server.stop()
    server.close()

if __name__ == "__main__":
    # server = pywsgi.WSGIServer(('0.0.0.0', 4090), handle_request, handler_class=WebSocketHandler)
    # signal.signal(signal.SIGINT, lambda num,info: shutdown(server))
    # print("Server Started")
    # server.serve_forever()
    APP.run(host='0.0.0.0', port=4090, debug=True)