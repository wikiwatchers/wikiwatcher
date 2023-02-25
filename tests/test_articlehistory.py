'''test for article history subclass'''
import __init__
import pytest
from articlehistory import ArticleHistory, format_timestamp


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
    art = ArticleHistory("Techno", None, None, ["mobile edit"])
    assert art.titles == "Techno"
    assert art.user == None
    assert art.keyword == None
    assert art.tags == ["mobile edit"]
    assert len(art.revisions) != 0

    art2 = ArticleHistory("", None, None, [""])
    assert art2.titles == ""
    assert art2.user == None
    assert art2.keyword == None
    assert art2.tags == [""]
    assert len(art2.revisions) == 0

    art3 = ArticleHistory("Salsa (Mexican Cuisine)", None, None, [""])
    assert art3.titles == "Salsa (Mexican Cuisine)"
    assert art3.user == None
    assert art3.keyword == None
    assert art3.tags == [""]
    assert len(art3.revisions) == 0

    art4 = ArticleHistory("Cat", "Greatgiant19", None, ["mw-reverted"])
    assert art4.titles == "Cat"
    assert art4.user == "Greatgiant19"
    assert art4.keyword == None
    assert art4.tags == ["mw-reverted"]
    assert len(art4.revisions) != 0


def test_filter_by_keyword():
    art = ArticleHistory("Techno", None, "techno")
    assert art.titles == "Techno"
    assert art.user == None
    assert art.keyword == "techno"
    assert art.tags == None
    assert len(art.revisions) != 0

    art2 = ArticleHistory("Techno", "Rio65trio", "techno")
    assert art2.titles == "Techno"
    assert art2.user == "Rio65trio"
    assert art2.keyword == "techno"
    assert art2.tags == None
    assert len(art2.revisions) != 0

    art3 = ArticleHistory("Cat", None, "gibberish")
    assert art3.titles == "Cat"
    assert art3.user == None
    assert art3.keyword == "gibberish"
    assert art3.tags == None
    assert len(art3.revisions) == 0

    art4 = ArticleHistory("Techno", "185.216.15.213",
                          "techno", ["mw-reverted"])
    assert art4.titles == "Techno"
    assert art4.user == "185.216.15.213"
    assert art4.keyword == "techno"
    assert art4.tags == ['mw-reverted']
    assert len(art4.revisions) != 0


def test_filter():
    art = ArticleHistory("Techno")
    assert art.tags == None
    assert art.keyword == None


if __name__ == "__main__":
    test___init__()
