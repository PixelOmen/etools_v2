from pathlib import Path
from datetime import datetime
from typing import TYPE_CHECKING
from dataclasses import dataclass

from .filesystem import server_path, server_cert, server_dkdm

if TYPE_CHECKING:
    from ..config import Config

HTML_DATE_FORMAT = "%Y-%m-%dT%H:%M"
SERVER_DATE_FORMAT = "%d/%m/%Y %H:%M"

@dataclass
class KDMSession:
    config: "Config"
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
    html_start: str = ''
    html_end: str = ''
    server_cert: str = ''
    server_dkdm: str = ''
    server_outputdir: str = ''

    def __post_init__(self):
        if self.start:
            self.html_start = self.start
            self.start = self._html_to_server_date(self.start)
        if self.end:
            self.html_end = self.end
            self.end = self._html_to_server_date(self.end)
        if self.cert:
            self.server_cert = server_cert(self.config, self.cert)
        if self.dkdm:
            self.server_dkdm = server_dkdm(self.config, self.dkdm)
        if self.outputDir:
            self.server_outputdir = server_path(Path(self.outputDir))

    def as_dict(self) -> dict:
        return {k:v for k,v in self.__dict__.items() if k != "config"}

    def validate(self) -> None:
        if self.status != "ok":
            return
        if not self._validate_sources():
            return
        if not self._validate_dates():
            return
        if not self._validate_output_dir():
            return

    def cli_cmd(self) -> str:
        # r' -C "CERT.pem" -K "outputname" -o "OUTPUTDIR" -f "2024-03-21T17:41:00-07:00" -t "2024-03-21T19:41:00-07:00" "DKDM.xml"'
        dkdm_name_frag = "_".join(Path(self.server_dkdm).stem.split("_")[1:])
        outputname = f"KDM_{dkdm_name_frag}_{Path(self.server_cert).stem}"

        clibin = f'"{self.config.clibin}"'
        start, end = self._cli_dates()
        cert = f'"{self.server_cert}"'
        dkdm = f'"{self.server_dkdm}"'
        outputdir = f'"{self.server_outputdir}"'
        return f"{clibin} -C {cert} -K {outputname} -o {outputdir} -f {start} -t {end} {dkdm}"

    def _cli_dates(self) -> tuple[str, str]:
        tz_prefix = self.timezone[0]
        tz_padding = f"{int(self.timezone[1:]):02}:00"
        tz = tz_prefix + tz_padding
        start = f'"{self.html_start + tz}"'
        end = f'"{self.html_end + tz}"'
        return start, end
    
    def _html_to_server_date(self, datestr: str) -> str:
        dateobj = datetime.strptime(datestr, HTML_DATE_FORMAT)
        return dateobj.strftime(SERVER_DATE_FORMAT)
        
    def _seterror(self, msg: str) -> None:
        self.status = "error"
        self.error = msg
    
    def _validate_sources(self) -> bool:
        if self.cert:
            if not Path(self.server_cert).is_file():
                self._seterror(f"Invalid Cert path: {self.server_cert}")
                return False
        if self.dkdm:
            if not Path(self.server_dkdm).is_file():
                self._seterror(f"Invalid DKDM path: {self.server_dkdm}")
                return False
        return True
    
    def _validate_output_dir(self) -> bool:
        if not Path(self.server_outputdir).is_dir():
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
    

    