""" Tests for user history class """
import __init__
from userhistory import UserHistory

def test_userhistory_init():
    """Tests user history init"""
    user_history = UserHistory("QuicoleJR", startyear=2023, startmonth=1,
                               startday=1, endyear=2023, endmonth=3, endday=1)

    assert user_history.user == "QuicoleJR"
    assert user_history.tags is None
    assert user_history.keyword is None
    assert len(user_history.revisions) > 0

def test_userhistory_tag_filter():
    """Tests user history filtering"""
    user_history = UserHistory("QuicoleJR", tags=["mobile edit"], startyear=2023, startmonth=1,
                               startday=1, endyear=2023, endmonth=3, endday=1)
    assert user_history.user == "QuicoleJR"
    assert len(user_history.tags) == 1
    assert user_history.tags[0] == "mobile edit"
    assert len(user_history.revisions) > 0
    assert "mobile edit" in user_history.revisions[0].tags

    user_history2 = UserHistory("QuicoleJR", tags=["spam"], startyear=2023, startmonth=1,
                               startday=1, endyear=2023, endmonth=2, endday=25)
    assert len(user_history2.revisions) == 0

def test_userhistory_keyword_filters():
    """Tests user history filtering"""
    user_history = UserHistory("QuicoleJR", keyword="cat", startyear=2023, startmonth=1,
                               startday=1, endyear=2023, endmonth=2, endday=25)

    assert user_history.user == "QuicoleJR"
    assert user_history.keyword == "cat"
    assert len(user_history.revisions) > 0
    assert user_history.revisions[0].contains_keyword("cat")

    user_history2 = UserHistory("QuicoleJR", keyword="bananas", startyear=2023, startmonth=1,
                               startday=1, endyear=2023, endmonth=2, endday=25)
    assert len(user_history2.revisions) == 0

def test_userhistory_timestamps():
    """Tests user history with timestamps"""
    user_history = UserHistory(user="Greatgiant19", startyear=2023, startmonth=2, startday=1,
                          endyear=2023, endmonth=2, endday=28)

    assert len(user_history.revisions) > 0
    assert user_history.user == "Greatgiant19"
    assert user_history.revisions[0].user == "Greatgiant19"
    assert user_history.revisions[0].title == "Bernie Ecclestone"


if __name__ == "__main__":
    test_userhistory_keyword_filter()
