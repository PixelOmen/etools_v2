from pathlib import Path
from collections import deque

from libs import dcpomatic, webfs
from libs.config import get_config

from filescanner import Scanner
from rosettapath import RosettaPath

# config = get_config()
# dcpomatic.set_config(config)

# TEST_REQUEST = {
#     "cert": "Burbank_Doremi_dcp2000-291790.cert.sha256.pem",
#     "dkdm": "DKDM_StopMakingSens_FTR-1_F_EN-XX_US_51_4K_A24_20230720_REI_IOP_OV.xml",
#     "startDate": "2025-01-01T01:00",
#     "endDate": "2025-01-02T01:00",
#     "timezone": "-11",
#     "outputDir": r"mnt\rei08\outputtest",
# }

testpath = r"C:\Users\eman\Projects\_testfiles\kdm_testing\rei08"

result = webfs.get_dir(testpath)

print(result)