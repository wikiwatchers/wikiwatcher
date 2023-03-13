''' Tests for user history class '''
import __init__
from userhistory import UserHistory

def test_userhistory_init():
    '''Tests user history init'''
    user_history = UserHistory("QuicoleJR")

    assert user_history.user == "QuicoleJR"
    assert user_history.tags is None
    assert user_history.keyword is None
    assert len(user_history.revisions) > 0

def test_userhistory_tag_filter():
    '''Tests user history filtering'''
    user_history = UserHistory("QuicoleJR", tags=["mobile edit"])
    assert user_history.user == "QuicoleJR"
    assert len(user_history.tags) == 1
    assert user_history.tags[0] == "mobile edit"
    assert len(user_history.revisions) > 0
    assert "mobile edit" in user_history.revisions[0].tags

def test_userhistory_keyword_filter():
    '''Tests user history filtering'''
    user_history = UserHistory("QuicoleJR", keyword="milk")

    assert user_history.user == "QuicoleJR"
    assert user_history.keyword == "milk"
    assert len(user_history.revisions) > 0
    assert user_history.revisions[0].contains_keyword("milk")

def test_userhistory_timestamps():
    '''Tests user history with timestamps'''
    user_history = UserHistory(user="Greatgiant19", startyear=2023, startmonth=2, startday=1,
                          endyear=2023, endmonth=2, endday=28)

    assert len(user_history.revisions) > 0
    assert user_history.user == "Greatgiant19"
    assert user_history.revisions[0].user == "Greatgiant19"
    assert user_history.revisions[0].title == "Bernie Ecclestone"


if __name__ == "__main__":
    test_userhistory_keyword_filter()
