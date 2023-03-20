"""test for article history subclass"""
import __init__
import pytest
from articlehistory import ArticleHistory
from exceptions import BadRequestException, NoRevisionsException

def test___init__():
    """tests initalization"""
    art1 = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    assert art1.titles == "Techno"
    assert art1.user == "Rio65trio"
    assert len(art1.revisions) == 35
    assert art1.pageid == 23958411
    assert art1.revisions[0].user == "Rio65trio"
    assert art1.revisions[22].title == "Techno"


    art = ArticleHistory(titles="Cat", startyear=2021, startmonth=2,
                         endyear=2021, endmonth=3)
    assert art.titles == "Cat"
    assert art.user is None
    assert len(art.revisions) != 0

    art = ArticleHistory(titles="Salsa", user="CAPTAIN RAJU",
                         startyear=2022, startmonth=2, startday=1,
                        endyear=2022, endmonth=2, endday=28)
    assert art.titles == "Salsa"
    assert art.user == "CAPTAIN RAJU"
    assert len(art.revisions) == 1
    assert art.revisions[0].user =="CAPTAIN RAJU"
    assert art.revisions[0].title =="Salsa"

    with pytest.raises(BadRequestException):
        art = ArticleHistory(titles=None)

def test_filter_by_tags():
    """tests filter by tags function"""
    art = ArticleHistory(titles="Techno", tags=["mobile edit"],
                         startyear=2023, startmonth=1, startday=1,
                        endyear=2023, endmonth=1, endday=30)
    assert art.titles == "Techno"
    assert art.user is None
    assert art.keyword is None
    assert art.tags == ["mobile edit"]
    assert len(art.revisions) == 1
    assert art.revisions[0].title == "Techno"
    assert art.revisions[0].tags[0] == "mobile edit"

    art2 = ArticleHistory(titles="", tags=[""])
    assert art2.titles == ""
    assert art2.user is None
    assert art2.keyword is None
    assert art2.tags == [""]
    assert len(art2.revisions) == 0

    art3 = ArticleHistory(titles="Salsa (Mexican Cuisine)", tags=[""],
                          startyear=2019, startmonth=12,
                          endyear=2020, endmonth=1)
    assert art3.titles == "Salsa (Mexican Cuisine)"
    assert art3.user is None
    assert art3.keyword is None
    assert art3.tags == [""]
    assert len(art3.revisions) == 0

    art4 = ArticleHistory(titles="Cat", user="Greatgiant19", tags=["mw-reverted"],
                          startyear=2023, startmonth=2, startday=1,
                          endyear=2023, endmonth=2, endday=28)
    assert art4.titles == "Cat"
    assert art4.user == "Greatgiant19"
    assert art4.keyword is None
    assert art4.tags == ["mw-reverted"]
    assert len(art4.revisions) == 1
    assert art4.revisions[0].user == "Greatgiant19"
    assert art4.revisions[0].title == "Cat"
    assert art4.revisions[0].tags[1] == "mw-reverted"


def test_filter_by_keyword():
    """tests filter by keyword function"""
    art2 = ArticleHistory(titles="Techno", user="Rio65trio", keyword="techno",
                          startyear=2022, startmonth=12, startday=1,
                          endyear=2022, endmonth=12, endday=30)
    assert art2.titles == "Techno"
    assert art2.user == "Rio65trio"
    assert art2.keyword == "techno"
    assert art2.tags is None
    assert len(art2.revisions) == 35
    assert art2.revisions[5].user == "Rio65trio"
    assert art2.revisions[27].title == "Techno"

    art3 = ArticleHistory(titles="Cat", keyword="gibberish",
                          startyear=2023, startmonth=1, startday=1,
                          endyear=2023, endmonth=1, endday=30)
    assert art3.titles == "Cat"
    assert art3.user is None
    assert art3.keyword == "gibberish"
    assert art3.tags is None
    assert len(art3.revisions) == 0

def test_filter():
    """tests filter function"""
    art = ArticleHistory(titles="Techno")
    assert art.tags is None
    assert art.keyword is None


if __name__ == "__main__":
    test_filter_by_keyword()
