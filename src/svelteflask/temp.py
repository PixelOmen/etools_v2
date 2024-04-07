from pathlib import Path

from libs import dcpomatic
from libs.config import get_config

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

# test = dcpomatic.process_request(TEST_REQUEST, "1")
# print(test.cli_cmd())


DKDM_PATH = r"D:\CodingProjects\_testfiles\kdm_testfiles\rei08\dkdms"

first = "DKDM_My_CTT_FOR_SOME_DCP"


for i in range(1, 10):
    testfile = f"{first}_{i}.xml"
    full_path = Path(DKDM_PATH) / testfile
    full_path.touch()