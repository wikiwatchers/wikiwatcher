'''Tests for class user revision'''
import json
import requests
from userHistory import UserHistory,  URL

def test_userhistory_init():
    '''Tests user history init'''
    userContribs = UserHistory("Jimbo Wales")

    assert userContribs.revisions[0].user == 'Jimbo Wales'
    assert userContribs.revisions[0].userid == 24

def test_userhistory_keyword():
    '''Tests user history with keyword'''
    assert 0 == 0
