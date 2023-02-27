'''test for article history subclass'''
import __init__
import pytest
from articlehistory import ArticleHistory, format_timestamp
from history import History

def test___init__():
    '''tests initalization'''
    art = ArticleHistory("Techno", "Rio65trio")
    assert art.titles == "Techno"
    assert art.user == "Rio65trio"
    assert len(art.revisions) != 0
    assert art.pageid == 23958411

    art = ArticleHistory("Cat")
    assert art.titles == "Cat"
    assert art.user is None
    assert len(art.revisions) != 0

    art = ArticleHistory("Salsa", "CAPTAIN RAJU")
    assert art.titles == "Salsa"
    assert art.user == "CAPTAIN RAJU"
    assert len(art.revisions) == 1

    art = ArticleHistory("fdjaklfgd;jsa")
    with pytest.raises(KeyError):
        raise KeyError("Data not found")

    art = ArticleHistory("")
    with pytest.raises(KeyError):
        raise KeyError("Data not found")

def test_filter_by_tags():
    '''tests filter by tags function'''
    art = ArticleHistory("Techno", None, None, ["mobile edit"],
                         2023, 1, 1, None, None, None, 2023, 1, 30)
    assert art.titles == "Techno"
    assert art.user is None
    assert art.keyword is None
    assert art.tags == ["mobile edit"]
    assert len(art.revisions) != 0

    art2 = ArticleHistory("", None, None, [""])
    assert art2.titles == ""
    assert art2.user is None
    assert art2.keyword is None
    assert art2.tags == [""]
    assert len(art2.revisions) == 0

    art3 = ArticleHistory("Salsa (Mexican Cuisine)", None, None, [""])
    assert art3.titles == "Salsa (Mexican Cuisine)"
    assert art3.user is None
    assert art3.keyword is None
    assert art3.tags == [""]
    assert len(art3.revisions) == 0

    art4 = ArticleHistory("Cat", "Greatgiant19", None, ["mw-reverted"],
                          2023, 2, 1, None, None, None, 2023, 2, 30)
    assert art4.titles == "Cat"
    assert art4.user == "Greatgiant19"
    assert art4.keyword is None
    assert art4.tags == ["mw-reverted"]
    assert len(art4.revisions) != 0


def test_filter_by_keyword():
    '''tests filter by keyword function'''
    art = ArticleHistory("Techno", None, "techno")
    assert art.titles == "Techno"
    assert art.user is None
    assert art.keyword == "techno"
    assert art.tags is None
    assert len(art.revisions) != 0

    art2 = ArticleHistory("Techno", "Rio65trio", "techno",
                          2022,12,1,None,None,None,2022,12,30)
    assert art2.titles == "Techno"
    assert art2.user == "Rio65trio"
    assert art2.keyword == "techno"
    assert art2.tags is None
    assert len(art2.revisions) != 0

    art3 = ArticleHistory("Cat", None, "gibberish")
    assert art3.titles == "Cat"
    assert art3.user is None
    assert art3.keyword == "gibberish"
    assert art3.tags is None
    assert len(art3.revisions) == 0

    art4 = ArticleHistory("Techno", "185.216.15.213",
                          "techno", ["mw-reverted"], 2022,11,1,
                          None, None, None, 2022,11,30)
    assert art4.titles == "Techno"
    assert art4.user == "185.216.15.213"
    assert art4.keyword == "techno"
    assert art4.tags == ['mw-reverted']
    assert len(art4.revisions) != 0


def test_filter():
    '''tests filter function'''
    art = ArticleHistory("Techno")
    assert art.tags is None
    assert art.keyword is None


if __name__ == "__main__":
    test___init__()
