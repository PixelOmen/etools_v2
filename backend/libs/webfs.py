import dataclasses
from pathlib import Path
import subprocess as sub
from dataclasses import dataclass

from .config import RosettaPath, CONFIG

@dataclass
class BrowserItem:
    displayName: str
    isDir: bool
    filePath: str

@dataclass
class DirResponse:
    dirPath: str
    parentPath: str
    contents: list[BrowserItem]
    status: str = "ok"
    error: str = ""

    def asdict(self) -> dict:
        return dataclasses.asdict(self)
    

def bad_request(dirpath: str, errmsg: str) -> DirResponse:
    return DirResponse(
        dirPath=dirpath,
        parentPath="",
        contents=[],
        status="error",
        error=errmsg
    )

def get_dir(dirpath: str) -> dict:
    if dirpath.lower() == "root" or dirpath.lower() == "mnt":
        if CONFIG.server.startswith("\\\\"):
            return DirResponse(
                dirPath="ROOT",
                parentPath="ROOT",
                contents=_build_contents_shares()
            ).asdict()            
        else:
            dirpath = "\\"

    server_path = Path(RosettaPath(dirpath).server_path())
    if dirpath == "\\" or server_path.parent == server_path:
        parent_path = "ROOT"
    else:
        if server_path.parent == Path(CONFIG.server):
            parent_path = "ROOT"
        else:
            parent_path = RosettaPath(server_path.parent).linux_path()
    linux_path = RosettaPath(dirpath).linux_path()

    if not server_path.is_dir():
        return bad_request(linux_path, f"Invalid directory:\n {dirpath}").asdict()
    
    return DirResponse(
        dirPath=linux_path,
        parentPath=parent_path,
        contents=_build_contents(server_path)
    ).asdict()


def _build_contents(dirpath: Path) -> list[BrowserItem]:
    items = []
    for item in dirpath.iterdir():
        if item.name[0] == ".":
            continue
        items.append(BrowserItem(
            displayName=item.name,
            isDir=item.is_dir(),
            filePath=RosettaPath(item).linux_path()
        ))
    return items

def _build_contents_shares() -> list[BrowserItem]:
    shares = _root_shares(CONFIG.server)
    items = []
    for item in shares:
        filepath = CONFIG.server + f"/{item}"
        items.append(BrowserItem(
            displayName=item,
            isDir=True,
            filePath=RosettaPath(filepath).linux_path()
        ))
    return items

def _root_shares(serverip: str) -> list[str]:
    cmd = ["net", "view", serverip, "/ALL"]
    result = sub.run(cmd, capture_output=True, text=True, check=True)
    output = result.stdout.split("\n")

    parsed = []
    share_break = False
    for line in output:
        if not share_break:
            if line.startswith("---"):
                share_break = True
            continue
        if line.startswith("The ") or "$" in line or not line:
            continue
        parsed.append(line.split(" ")[0].strip())
    return parsed