'''test for article history subclass'''
import __init__
import pytest
from articlehistory import ArticleHistory, format_timestamp

def test___init__():
    '''tests initalization'''
    art = ArticleHistory("Techno", "Rio65trio")
    assert art.titles == "Techno"
    assert art.user == "Rio65trio"
    assert len(art.revisions) == 10
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
        
def test_format_timestamp():
    """ tests module level function for creating timestamp string from ints"""
    t_revisions = ArticleHistory("test")
    # full datetime
    assert format_timestamp(2008, 6, 7, 4, 1, 30) == '20080607040130'
    # partials to do

if __name__ == "__main__":
    test___init__()