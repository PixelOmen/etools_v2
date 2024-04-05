import dataclasses
import subprocess as sub
from pathlib import Path
from datetime import datetime
from typing import TYPE_CHECKING

from rosettapath import RosettaPath

if TYPE_CHECKING:
    from ..config import Config

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
    html_start: str = dataclasses.field(init=False)
    html_end: str = dataclasses.field(init=False)

    def __post_init__(self):
        if self.start:
            self.html_start = self.start
            self.start = self._html_to_server_date(self.start)
        if self.end:
            self.html_end = self.end
            self.end = self._html_to_server_date(self.end)            

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)

    def validate(self, config: "Config") -> None:
        if self.status != "ok":
            return
        if not self._validate_sources(config):
            return
        if not self._validate_dates():
            return
        if not self._validate_output_dir():
            return

    def cli_cmd(self, config: "Config") -> str:
        start, end = self._cli_dates()
        clibin = f'"{config.clibin}"'
        # r' -C "CERT.pem" -K "outputname" -o "OUTPUTDIR" -f "2024-03-21T17:41:00-07:00" -t "2024-03-21T19:41:00-07:00" "DKDM.xml"'
        return ""

    def _cli_dates(self) -> tuple[str, str]:
        tz_prefix = self.timezone[0]
        tz_padding = f"{int(self.timezone[1:]):02}:00"
        tz = tz_prefix + tz_padding
        start = self.html_start + tz
        end = self.html_end + tz
        return start, end
    
    def _html_to_server_date(self, datestr: str) -> str:
        dateobj = datetime.strptime(datestr, HTML_DATE_FORMAT)
        return dateobj.strftime(SERVER_DATE_FORMAT)
        
    def _seterror(self, msg: str) -> None:
        self.status = "error"
        self.error = msg
    
    def _validate_sources(self, config: "Config") -> bool:
        if self.cert:
            serverpath = RosettaPath(config.certdir / self.cert).server_path()
            if not Path(serverpath).is_file():
                self._seterror(f"Invalid Cert path: {serverpath}")
                return False
        if self.dkdm:
            serverpath = RosettaPath(config.dkdmdir / self.dkdm).server_path()
            if not Path(serverpath).is_file():
                self._seterror(f"Invalid DKDM path: {serverpath}")
                return False            
        return True
    
    def _validate_output_dir(self) -> bool:
        outputdir = Path(RosettaPath(Path(self.outputDir)).server_path())
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
    

    