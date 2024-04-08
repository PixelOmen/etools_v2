from pathlib import Path
from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from .config import RosettaPath

if TYPE_CHECKING:
    from .config import Config

ACCEPTED_CERT_EXTS = [".pem", ".cert", ".crt"]
ACCEPTED_DKDM_EXTS = [".xml"]

@dataclass
class ListItemData:
    pathobj: Path
    displayName: str = field(init=False)
    isFile: bool = field(init=False)
    isDir: bool = field(init=False)

    def __post_init__(self):
        self.displayName = str(self.pathobj.name)
        self.isFile = self.pathobj.is_file()
        self.isDir = self.pathobj.is_dir()

    def as_dict(self) -> dict:
        return {
            "displayName": self.displayName,
            "isFile": self.isFile,
            "isDir": self.isDir
        }

def get_certs(rootdir: str|Path) -> list[dict]:
    certs = []
    rootdir = Path(rootdir)
    for item in rootdir.iterdir():
        if (item.name[0] == "." or 
            (item.is_file() and
            item.suffix.lower() not in ACCEPTED_CERT_EXTS)):
            continue
        certs.append(ListItemData(item).as_dict())
    return certs

def get_dkdms(rootdir: str|Path) -> list[dict]:
    certs = []
    rootdir = Path(rootdir)
    for item in rootdir.iterdir():
        if (not item.is_file() or
            item.name[0] == "." or
            not item.name.lower().startswith("dkdm") or
            item.suffix.lower() not in ACCEPTED_DKDM_EXTS):
            continue
        certs.append(ListItemData(item).as_dict())
    return certs


def server_path(userpath: Path) -> str:
    return RosettaPath(userpath).server_path()

def server_cert(config: "Config", certname: str) -> str:
    return server_path(config.certdir / certname)

def server_dkdm(config: "Config", dkdmname: str) -> str:
    return server_path(config.dkdmdir / dkdmname)