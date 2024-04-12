import dataclasses
from pathlib import Path
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
        dirpath = "\\"
    server_path = Path(RosettaPath(dirpath).server_path())
    if dirpath == "\\":
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