from typing import Any
from pathlib import Path

def _validate_dir(rootdir: Path) -> dict:
    if not rootdir.is_dir():
        return {"Status": "Error",
                "error": f"Not a valid directory: {rootdir}"}
    return {}

def process_request(userinput: Any) -> dict:
    if not isinstance(userinput, dict):
        return {"Status": "Error", "error": "Malformed JSON in `process_request`"}
    outputdir = Path(userinput["outputDir"])
    error = _validate_dir(outputdir)
    if error:
        return error
    return {"Status": "ok"}