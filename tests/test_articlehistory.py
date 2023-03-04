"""test for article history subclass"""
import __init__
import pytest
from articlehistory import ArticleHistory, format_timestamp
from history import History

def test___init__():
    """tests initalization"""
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    assert art.titles == "Techno"
    assert art.user == "Rio65trio"
    assert len(art.revisions) != 0
    assert art.pageid == 23958411

    art = ArticleHistory(titles="Cat")
    assert art.titles == "Cat"
    assert art.user is None
    assert len(art.revisions) != 0

    art = ArticleHistory(titles="Salsa", user="CAPTAIN RAJU",
                         startyear=2022, startmonth=2, startday=1,
                        endyear=2022, endmonth=2, endday=28)
    assert art.titles == "Salsa"
    assert art.user == "CAPTAIN RAJU"
    assert len(art.revisions) == 1

    art = ArticleHistory(titles="fdjaklfgd;jsa")
    with pytest.raises(KeyError):
        raise KeyError("Data not found")

    art = ArticleHistory(titles="")
    with pytest.raises(KeyError):
        raise KeyError("Data not found")

def test_filter_by_tags():
    """tests filter by tags function"""
    art = ArticleHistory(titles="Techno", tags=["mobile edit"],
                         startyear=2023, startmonth=1, startday=1,
                        endyear=2023, endmonth=1, endday=30)
    assert art.titles == "Techno"
    assert art.user is None
    assert art.keyword is None
    assert art.tags == ["mobile edit"]
    assert len(art.revisions) != 0

    art2 = ArticleHistory(titles="", tags=[""])
    assert art2.titles == ""
    assert art2.user is None
    assert art2.keyword is None
    assert art2.tags == [""]
    assert len(art2.revisions) == 0

    art3 = ArticleHistory(titles="Salsa (Mexican Cuisine)", tags=[""])
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
    assert len(art4.revisions) != 0


def test_filter_by_keyword():
    """tests filter by keyword function"""
    art = ArticleHistory(titles="Techno", keyword="Berlin",
                         startyear=2022, startmonth=12, startday=1,
                         endyear=2022, endmonth=12, endday=30)
    assert art.titles == "Techno"
    assert art.user is None
    assert art.keyword == "Berlin"
    assert art.tags is None
    assert len(art.revisions) != 0

    art2 = ArticleHistory(titles="Techno", user="Rio65trio", keyword="techno",
                          startyear=2022, startmonth=12, startday=1,
                          endyear=2022, endmonth=12, endday=30)
    assert art2.titles == "Techno"
    assert art2.user == "Rio65trio"
    assert art2.keyword == "techno"
    assert art2.tags is None
    assert len(art2.revisions) != 0

    art3 = ArticleHistory(titles="Cat", keyword="gibberish",
                          startyear=2023, startmonth=1, startday=1,
                          endyear=2023, endmonth=1, endday=30)
    assert art3.titles == "Cat"
    assert art3.user is None
    assert art3.keyword == "gibberish"
    assert art3.tags is None
    assert len(art3.revisions) == 0

    art4 = ArticleHistory(titles="Techno", user="185.216.15.213",
                          keyword="techno", tags=["mw-reverted"],
                          startyear=2022, startmonth=11, startday=1,
                          endyear=2022, endmonth=11, endday=30)
    assert art4.titles == "Techno"
    assert art4.user == "185.216.15.213"
    assert art4.keyword == "techno"
    assert art4.tags == ["mw-reverted"]
    assert len(art4.revisions) != 0


def test_filter():
    """tests filter function"""
    art = ArticleHistory(titles="Techno")
    assert art.tags is None
    assert art.keyword is None


if __name__ == "__main__":
    test_filter_by_keyword()
