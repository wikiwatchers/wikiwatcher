""" Tests for user history class """
import __init__
from userhistory import UserHistory

def test_userhistory_init():
    """Tests user history init"""
    # specifying a short date range prevents unnecessarily pulling down
    # a very large number of revisions - saves us time on testing
    user_history = UserHistory("Jimbo Wales",
                               startyear=2022, startmonth=1, startday=1,
                               endyear=2022, endmonth=1, endday=1)

    assert user_history.user == "Jimbo Wales"

def test_userhistory_tag_filter():
    """Tests user history filtering"""
    user_history = UserHistory("Jimbo Wales",
                               startyear=2021, startmonth=5,
                               endyear=2021, endmonth=7,
                               tags=["mw-reverted"])

    assert len(user_history.revisions) == 3

def test_userhistory_keyword_filter():
    """Tests user history filtering"""
    user_history = UserHistory("Jimbo Wales", keyword="radio",
                               startyear=2020, startmonth=4,
                               endyear=2020, endmonth=5)

    assert len(user_history.revisions) == 3

if __name__ == "__main__":
    test_userhistory_keyword_filter()
