import json

def navlinks() -> str:
    navdict = [
        {
            "sectionName" : "Rendering",
            "contents": [
                {
                    "url": "http://etools01.rndbtprvt.lan/external/Render/10.0.20.96:4040",
                    "displayName": "Create"
                },
                {
                    "url": "http://10.0.10.146/cf-web-ui/render",
                    "displayName": "Status"
                }                
            ]
        },
        {
            "sectionName" : "Reports",
            "contents": [
                {
                    "url": "http://etools01.rndbtprvt.lan/external/Schedule/10.0.30.24:80/callsheetbydate",
                    "displayName": "Schedule"
                }
            ]
        },
        {
            "sectionName" : "File Tools",
            "contents": [
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/audioflag",
                    "displayName": "Flag Audio"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/setTC",
                    "displayName": "Set TC"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/dvmeta",
                    "displayName": "Validate DV"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/dvhr0",
                    "displayName": "DV Hour 0"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/ltolabels",
                    "displayName": "LTO Labels"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/filediff",
                    "displayName": "File Diff"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/calc",
                    "displayName": "TC Calc"
                },
                {
                    "url": "http://etools01.rndbtprvt.lan/tools/ioextract",
                    "displayName": "PDF Extract"
                },                
            ]
        },
        {
            "sectionName" : "San Tools",
            "contents": [
                {
                    "url": "http://10.0.20.6",
                    "displayName": "ARC"
                },              
                {
                    "url": "http://10.0.20.103",
                    "displayName": "SIGHT"
                }
            ]
        }
    ]
    return json.dumps(navdict)