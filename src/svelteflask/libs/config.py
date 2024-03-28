import json
from pathlib import Path
from dataclasses import dataclass

JSONPATH = Path(__file__).parent.parent / "config.json"

@dataclass
class Config:
    certdir: Path
    dkdmdir: Path

def _verify_keys(jdict: dict, keys: list[str]) -> dict:
    valid_dict = {}
    for k in keys:
        value = jdict.get(k)
        if value is None:
            raise KeyError(f"Missing key in config.json: {k}")
        valid_dict[k] = value
    return valid_dict

def get_config() -> Config:
    keys = ["certdir", "dkdmdir"]
    with open(JSONPATH, 'r') as fp:
        jdict = json.loads(fp.read())
    valid_dict = _verify_keys(jdict, keys)
    return Config(
        certdir=valid_dict["certdir"],
        dkdmdir=valid_dict["dkdmdir"]
    )