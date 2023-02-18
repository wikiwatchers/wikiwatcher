'''Tests for class user revision'''
import json
import requests
from userhistory import UserHistory,  URL
with open('user_test.json', 'r', encoding='utf-8') as q:
    TPARAMS = json.load(q)

# pylint: disable=W0603,W0602

T_UREVS = None

def test_userhistory_init():
    '''Tests userrevision init'''
    global T_UREVS, TPARAMS
    j = requests.get(URL, TPARAMS).json()
    userrevjson = j["query"]["usercontribs"]
    T_UREVS = UserHistory(userrevjson)
    assert T_UREVS.revisions[0].user == 'Jimbo Wales'
    assert T_UREVS.revisions[0].userid == 24
