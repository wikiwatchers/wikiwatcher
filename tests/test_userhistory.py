''' Tests for user history class '''
import __init__
from userhistory import UserHistory

def test_userhistory_init():
    '''Tests user history init'''
    user_history = UserHistory("Jimbo Wales")

    assert user_history.user == "Jimbo Wales"

def test_userhistory_tag_filter():
    '''Tests user history filtering'''
    user_history = UserHistory("Jimbo Wales", tags=["discussiontools-newtopic"])

    assert user_history.user == "Jimbo Wales"
    assert len(user_history.tags) == 1
    assert user_history.tags[0] == "discussiontools-newtopic"

def test_userhistory_keyword_filter():
    '''Tests user history filtering'''
    user_history = UserHistory("Jimbo Wales", keyword="Duplicate page")

    assert user_history.user == "Jimbo Wales"
    assert user_history.keyword == "Duplicate page"
