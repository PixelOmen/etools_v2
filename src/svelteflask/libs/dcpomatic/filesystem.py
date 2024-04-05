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
    filePath: str = field(init=False)
    displayName: str = field(init=False)

    def __post_init__(self):
        self.filePath = str(self.pathobj)
        self.displayName = str(self.pathobj.name)

    def as_dict(self) -> dict:
        return {
            "filePath": self.filePath,
            "displayName": self.displayName
        }

def get_certs(rootdir: str|Path) -> list[dict]:
    certs = []
    rootdir = Path(rootdir)
    for item in rootdir.iterdir():
        if (not item.is_file() or
            item.name[0] == "." or
            item.suffix.lower() not in ACCEPTED_CERT_EXTS):
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