import json
from pathlib import Path
from dataclasses import dataclass

JSONPATH = Path(__file__).parent.parent / "config.json"
KEYS = ["certdir", "dkdmdir", "clibin", "server"]

@dataclass
class Config:
    certdir: Path
    dkdmdir: Path
    clibin: Path
    server: str


def _verify_keys(jdict: dict, keys: list[str]) -> dict:
    valid_dict = {}
    for k in keys:
        value = jdict.get(k)
        if value is None:
            raise KeyError(f"Missing key in config.json: {k}")
        valid_dict[k] = value
    return valid_dict

def get_kdm_config() -> Config:
    with open(JSONPATH, 'r') as fp:
        jdict = json.loads(fp.read())
    valid_dict = _verify_keys(jdict, KEYS)
    return Config(
        certdir=Path(valid_dict["certdir"]),
        dkdmdir=Path(valid_dict["dkdmdir"]),
        clibin=Path(valid_dict["clibin"]),
        server=valid_dict["server"]
    )