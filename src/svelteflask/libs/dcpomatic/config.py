from rosettapath import RosettaPath

from ..config import Config

CONFIG: Config | None = None

def set_config(config: Config) -> None:
    global CONFIG
    CONFIG = config
    RosettaPath.default_server_prefix = CONFIG.server
    if CONFIG.server == "C:\\":
        RosettaPath.input_mount_patterns['server'] = r"^C:"
        

def get_config() -> Config:
    if CONFIG is None:
        raise RuntimeError("CONFIG not set in dcpomatic module")
    return CONFIG