import json

def navlinks() -> str:
    navdict = [
        {
            "sectionName" : "Rendering",
            "contents": [
                {
                    "url": "localhost:4090",
                    "displayName": "Create"
                },
                {
                    "url": "localhost:4090",
                    "displayName": "Status"
                }                
            ]
        },
        {
            "sectionName" : "Reports",
            "contents": [
                {
                    "url": "/another",
                    "displayName": "Schedule"
                }
            ]
        },
        {
            "sectionName" : "File Tools",
            "contents": [
                {
                    "url": "/another",
                    "displayName": "Another"
                }
            ]
        },
        {
            "sectionName" : "San Tools",
            "contents": [
                {
                    "url": "/another",
                    "displayName": "Another"
                }
            ]
        }
    ]
    return json.dumps(navdict)