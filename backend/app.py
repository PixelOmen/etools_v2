import uuid
import signal
import mimetypes
from typing import Callable
from datetime import datetime
from collections import deque

import requests

from flask import (
    Flask, Response,
    request, session,
    send_from_directory,
)
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from libs import dcpomatic, webfs
from libs.navlib import NAVLINKS
from libs.config import get_config

CONFIG = get_config()

PULSELIB_PORT = 80

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

def forward_get_request(url: str) -> Response:
    res = requests.get(url)
    return Response(res.content, status=res.status_code, headers=dict(res.headers))

def forward_post_request(url: str, jdict: dict) -> Response:
    res = requests.post(url=url, json=jdict)
    return Response(res.content, status=res.status_code, headers=dict(res.headers))

def pywsgi_handle_request(environ: dict, start_response: Callable):
    return APP(environ, start_response)


@APP.route('/api/nextdate')
def nextdate():
    return forward_get_request(f"http://10.0.30.24:{PULSELIB_PORT}/api/nextdate")

@APP.route('/api/schedulestats')
def schedulestats():
    return forward_get_request(f"http://10.0.30.24:{PULSELIB_PORT}/api/schedulestats")

@APP.route('/api/callsheet_query', methods=["POST"])
def callsheeet_query():
    return forward_post_request(f"http://10.0.30.24:{PULSELIB_PORT}/callsheet_query", request.get_json())

@APP.route('/api/callsheet_pdf/<string:filename>')
def send_pdf(filename: str):
    return forward_get_request(f"http://10.0.30.24:{PULSELIB_PORT}/callsheetbydate/{filename}")

@APP.route("/api/webfs", methods=["POST"])
def webfs_request():
    if request.method != "POST":
        return Response(status=400)    

    try:
        jdict = request.json
        userpath = jdict["path"] #type:ignore
    except Exception as e:
        return webfs.bad_request("", f"Unable to parse JSON: {str(e)}").asdict()
        
    return webfs.get_dir(userpath)

@APP.route('/api/nav')
def nav():
    return NAVLINKS

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
    # server = pywsgi.WSGIServer(('0.0.0.0', 4090), pywsgi_handle_request, handler_class=WebSocketHandler)
    # signal.signal(signal.SIGINT, lambda num,info: shutdown(server))
    # print("Server Started")
    # server.serve_forever()
    APP.run(host='0.0.0.0', port=4090, debug=True)