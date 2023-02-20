'''Tests for class user revision'''
import json
import requests

from userHistory import UserHistory,  URL

def test_userhistory_init():
    '''Tests user history init'''
    user_contribs = UserHistory("Jimbo Wales")

    assert user_contribs.revisions[0]['user'] == 'Jimbo Wales'
    assert user_contribs.revisions[0]['userid'] == 24
    assert len(user_contribs.revisions) == 10

    another_user_contribs = UserHistory("RobinHood70")

    assert another_user_contribs.revisions[0]['user'] == 'RobinHood70'
    assert another_user_contribs.revisions[0]['userid'] == 4859457
    assert len(another_user_contribs.revisions) == 10

def test_userhistory_keyword():
    '''Tests user history with keyword - TO DO after filtering'''
    keyword = "Talk:Archives of Venice"

    user_contribs = UserHistory('Jimbo Wales', keyword)

    print(user_contribs.revisions[8])

    assert user_contribs.revisions[8]['title'] == keyword
