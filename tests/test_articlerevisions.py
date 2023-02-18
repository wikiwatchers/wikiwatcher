""" to be merged in with nob/1 """

import __init__
from articlerevisions import ArticleRevisions

def test_format_timestamp():
    a = ArticleRevisions("test")
    # full datetime
    assert a.format_timestamp(2008, 6, 7, 4, 1, 30) == '20080607040130'
    # partials
    #assert a.format_timestamp(2008, 0, 7, 4, 1, 30) == '20080607040130'

if __name__ == "__main__":
    test_format_timestamp()