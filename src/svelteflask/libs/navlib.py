import json

def navlinks() -> str:
    navdict = [
        {
            "sectionName" : "Rendering",
            "contents": [
                {
                    "url": "/rendering/create",
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
                    "url": "/reports/schedule",
                    "displayName": "Schedule"
                }
            ]
        },
        {
            "sectionName" : "File Tools",
            "contents": [
                {
                    "url": "/filetools/audioflag",
                    "displayName": "Flag Audio"
                },
                {
                    "url": "/filetools/setTC",
                    "displayName": "Set TC"
                },
                {
                    "url": "/filetools/dvmeta",
                    "displayName": "Validate DV"
                },
                {
                    "url": "/filetools/dvhr0",
                    "displayName": "DV Hour 0"
                },
                {
                    "url": "/filetools/ltolabels",
                    "displayName": "LTO Labels"
                },
                {
                    "url": "/filetools/filediff",
                    "displayName": "File Diff"
                },
                {
                    "url": "/filetools/calc",
                    "displayName": "TC Calc"
                },
                {
                    "url": "/filetools/ioextract",
                    "displayName": "PDF Extract"
                },                
            ]
        },
        {
            "sectionName" : "San Tools",
            "contents": [
                {
                    "url": "10.0.20.6",
                    "displayName": "ARC"
                },              
                {
                    "url": "10.0.20.103",
                    "displayName": "SIGHT"
                }
            ]
        }
    ]
    return json.dumps(navdict)