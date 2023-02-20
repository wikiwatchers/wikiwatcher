import pytest
from history import History
from article_history import ArticleHistory

def test___init__():
    art = ArticleHistory("Techno", "Rio65trio")
    assert art.titles == "Techno"
    assert art.user == "Rio65trio"
    assert len(art.revisions) == 10
    assert art.pageid == 23958411
