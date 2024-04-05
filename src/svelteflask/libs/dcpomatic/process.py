import dataclasses
import subprocess as sub
from pathlib import Path
from datetime import datetime
from typing import Any, Union, TYPE_CHECKING

from .config import Config, get_config
from .kdmsession import KDMSession, SERVER_DATE_FORMAT

# --- fronend payload
# {
#     "cert": "somecert1",
#     "dkdm": "somedkdm1",
#     "startDate": "2025-01-01T01:00",
#     "endDate": "2025-01-01T01:00",
#     "timezone": "-11",
#     "outputDir": "mnt/my/output/dir",
# }

def process_request(userdata: Any, jobid: str) -> KDMSession:
    if not isinstance(userdata, dict):
        return _bad_request(jobid)
    kdmsession = _create_session(userdata, jobid)
    kdmsession.validate()
    if kdmsession.status == "ok":
        _start_subprocess(kdmsession)
    return kdmsession




def _start_subprocess(kdmsession: KDMSession) -> None:
    cmd = kdmsession.cli_cmd()

def _now_str() -> str:
    return datetime.now().strftime(SERVER_DATE_FORMAT)

def _bad_request(jobid: str) -> KDMSession:
    return KDMSession(
        config=get_config(),
        jobid=jobid,
        submitted=_now_str(),
        status='error',
        error='Malformed JSON from frontend'
    )
    
def _create_session(userdata: dict, jobid: str) -> KDMSession:
    try:
        start_str = userdata['startDate']
        end_str = userdata['endDate']
        cert = userdata['cert']
        dkdm = userdata['dkdm']
        timezone = userdata['timezone']
        outputDir = userdata['outputDir']
    except KeyError:
        return _bad_request(jobid)

    return KDMSession(
        config=get_config(),
        jobid=jobid,
        submitted=_now_str(),
        cert=cert,
        dkdm=dkdm,
        start=start_str,
        end=end_str,
        timezone=timezone,
        outputDir=outputDir
    )