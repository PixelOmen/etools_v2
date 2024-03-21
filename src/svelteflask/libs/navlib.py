import json

def navlinks() -> str:
    navdict = [
        {
            "sectionName" : "TestSection",
            "contents": [
                {
                    "url": "/another",
                    "displayName": "Another"
                }
            ]
        },
        {
            "sectionName" : "DifferentOne",
            "contents": [
                {
                    "url": "/another",
                    "displayName": "Another"
                }
            ]
        }
    ]
    return json.dumps(navdict)