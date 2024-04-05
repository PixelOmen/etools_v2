from libs import dcpomatic
from libs.config import get_kdm_config

from rosettapath import RosettaPath

config = get_kdm_config()
dcpomatic.set_config(config)

TEST_REQUEST = {
    "cert": "somecert1",
    "dkdm": "somedkdm1",
    "startDate": "2025-01-01T01:00",
    "endDate": "2025-01-01T01:00",
    "timezone": "-11",
    "outputDir": r"C:\Users\eman\Projects\_testfiles\output",
}

# test = dcpomatic.process_request(TEST_REQUEST, "1")
# print(test.error)

test = RosettaPath(TEST_REQUEST["outputDir"])
print(test.server_path())

