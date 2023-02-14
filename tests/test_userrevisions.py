'''Tests for class user revision'''
import __init__
import json
import requests
from userrevisions import UserRevisions,  URL

T_UREVS = None

def test_userrevision_init():
    '''Tests userrevision init'''
    global T_UREVS, TPARAMS
    TPARAMS = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": "Jimbo%20Wales"
        }
    j = requests.get(URL, TPARAMS).json()
    userrevjson = j['query']['allrevisions'][0]['revisions'][0]
    T_REV = UserRevisions(userrevjson)
    assert T_REV.user == 'Starfox'