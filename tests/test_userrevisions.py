'''Tests for class user revision'''
import json
import requests
from userrevisions import UserRevisions,  URL

T_UREVS = None

def test_userrevision_init():
    '''Tests userrevision init'''
    with open('user_test.json', 'r', encoding='utf-8') as q:
        test_params = json.load(q)
    j = requests.get(URL, test_params).json()
    userrevjson = j["query"]["usercontribs"]
    T_UREVS = UserRevisions(userrevjson)
    assert T_UREVS.revisions[0].user == 'Jimbo Wales'
    assert T_UREVS.revisions[0].userid == 24
