'''Tests for class user revision'''
import json
import requests
from userrevisions import UserRevisions,  URL
with open('user_test.json', 'r', encoding='utf-8') as q:
    TPARAMS = json.load(q)

T_UREVS = None

def test_userrevision_init():
    '''Tests userrevision init'''
    global T_UREVS, TPARAMS
    j = requests.get(URL, TPARAMS).json()
    print(j)
    userrevjson = j["query"]["usercontribs"]
    T_UREVS = UserRevisions(userrevjson)
    print(T_UREVS)
    assert T_UREVS.revisions[0].user == 'Jimbo Wales'