import subprocess as sub
from typing import Any
from pathlib import Path
from datetime import datetime

from ..config import get_config
from .filesystem import scan_for_certs, server_path
from .kdmsession import KDMSession, SERVER_DATE_FORMAT, HTML_DATE_FORMAT

# --- fronend payload
# {
#     "cert": {
#         "displayName": "somecert1",
#         "isDir": True,
#         "isFile": False
#     },
#     "dkdm": "somedkdm1",
#     "startDate": "2025-01-01T01:00",
#     "endDate": "2025-01-01T01:00",
#     "timezone": "-11",
#     "outputDir": "mnt/my/output/dir",
# }

def process_request(userdata: Any, jobid: str) -> list[KDMSession]:
    if not isinstance(userdata, dict):
        return [_bad_request(jobid)]
    kdmsessions = _create_sessions(userdata, jobid)
    for session in kdmsessions:
        session.validate()
        if session.status == "ok":
            _start_subprocess(session)
    return kdmsessions

def _start_subprocess(kdmsession: KDMSession) -> None:
    cmd = kdmsession.cli_cmd()
    process = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
    _, stderr = process.communicate()
    if stderr:
        stderr_str = stderr.decode()
        if stderr_str:
            try:
                error = stderr_str.split(f"{str(kdmsession.config.clibin)[1:-1]}: ")[1]
            except IndexError:
                error = stderr_str
            kdmsession.set_error(f"DCP-o-matic error:\n {error}")




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
    
def _create_sessions(userdata: dict, jobid: str) -> list[KDMSession]:
    try:
        start_str = userdata['startDate']
        end_str = userdata['endDate']
        usercert = userdata['cert']
        dkdm = userdata['dkdm']
        timezone = userdata['timezone']
        outputDir = userdata['outputDir']
    except KeyError:
        return [_bad_request(jobid)]

    cert_name = usercert.get("displayName")
    cert_is_file = usercert.get("isFile")
    if cert_name is None or cert_is_file is None:
        return [_bad_request(jobid)]
    
    config = get_config()
    submitted = _now_str()
    if cert_is_file:
        return [KDMSession(
            config=config,
            jobid=jobid,
            submitted=submitted,
            cert=cert_name,
            dkdm=dkdm,
            start=start_str,
            end=end_str,
            timezone=timezone,
            outputDir=outputDir
        )]
    else:
        err = _validate_group_output(outputDir)
        if err:
           return [_bad_group(jobid, userdata, err)]
        
        err = _validate_group_dates(start_str, end_str)
        if err:
           return [_bad_group(jobid, userdata, err)]
        
        certs = scan_for_certs(config.certdir / cert_name)
        if not certs:
            return [_bad_group(jobid, userdata, f"No certs found: {cert_name}")]

        sessions = []
        for cert in certs:
            sessions.append(KDMSession(
                config=config,
                jobid=jobid,
                submitted=submitted,
                cert=cert,
                dkdm=dkdm,
                start=start_str,
                end=end_str,
                timezone=timezone,
                outputDir=outputDir
            ))
        return sessions



def _validate_group_output(outputdir: str) -> str:
    if not Path(server_path(outputdir)).is_dir():
        return f"Not a valid directory: {outputdir}"
    return ""

def _validate_group_dates(userstart: str, userend: str) -> str:
    start = datetime.strptime(userstart, HTML_DATE_FORMAT)
    end = datetime.strptime(userend, HTML_DATE_FORMAT)
    if end <= start:
        return "End time is less than or equal to Start time"
    return ""

def _bad_group(jobid: str, userdata: dict, errormsg: str) -> KDMSession:
    start_str = userdata['startDate']
    end_str = userdata['endDate']
    usercert = userdata['cert']
    dkdm = userdata['dkdm']
    timezone = userdata['timezone']
    outputDir = userdata['outputDir']
    config = get_config()
    submitted = _now_str()
    return KDMSession(
        config=config,
        jobid=jobid,
        submitted=submitted,
        cert=usercert["displayName"],
        dkdm=dkdm,
        start=start_str,
        end=end_str,
        timezone=timezone,
        outputDir=outputDir,
        status="error",
        error=errormsg
    )