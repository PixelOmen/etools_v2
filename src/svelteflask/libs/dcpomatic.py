import dataclasses
from typing import Any
from pathlib import Path
from datetime import datetime

# {
#     "id": 1,
#     "cert": "somecert1",
#     "dkdm": "somedkdm1",
#     "submitted": "01/01/25T01:00",
#     "start": "01/01/25T01:00",
#     "end": "01/01/25T02:00",
#     "timezone": "-11",
#     "outputDir": "mnt/my/output/dir",
#     "status": "error",
#     "error": "From the first one"
# }

HTML_DATE_FORMAT = "%Y-%m-%dT%H:%M"
SERVER_DATE_FORMAT = "%d/%m/%Y %H:%M"

@dataclasses.dataclass
class KDMSession:
    jobid: str
    submitted: str
    cert: str = ''
    dkdm: str = ''
    start: str = ''
    end: str = ''
    timezone: str = ''
    outputDir: str = ''
    status: str = 'ok'
    error: str = ''

    def __post_init__(self):
        if self.start:
            self.start = self._html_to_server_date(self.start)
        if self.end:
            self.end = self._html_to_server_date(self.end)            

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)

    def validate(self) -> None:
        if self.status != "ok":
            return
        if not self._validate_dates():
            return
        if not self._validate_dir():
            return
        
    def _html_to_server_date(self, datestr: str) -> str:
        dateobj = datetime.strptime(datestr, HTML_DATE_FORMAT)
        return dateobj.strftime(SERVER_DATE_FORMAT)
        
    def _seterror(self, msg: str) -> None:
        self.status = "error"
        self.error = msg
    
    def _validate_dir(self) -> bool:
        outputdir = Path(self.outputDir)
        if not outputdir.is_dir():
            self._seterror(f"Not a valid directory: {self.outputDir}")
            return False
        return True

    def _validate_dates(self) -> bool:
        start = datetime.strptime(self.start, SERVER_DATE_FORMAT)
        end = datetime.strptime(self.end, SERVER_DATE_FORMAT)
        if end <= start:
            self._seterror("End time is less than or equal to Start time")
            return False
        return True



def process_request(userdata: Any, jobid: str) -> KDMSession:
    if not isinstance(userdata, dict):
        return _bad_request(jobid)
    kdmsession = _create_session(userdata, jobid)
    kdmsession.validate()
    return kdmsession


def _now_str() -> str:
    return datetime.now().strftime(SERVER_DATE_FORMAT)

def _bad_request(jobid: str) -> KDMSession:
    return KDMSession(
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
        jobid=jobid,
        submitted=_now_str(),
        cert=cert,
        dkdm=dkdm,
        start=start_str,
        end=end_str,
        timezone=timezone,
        outputDir=outputDir
    )