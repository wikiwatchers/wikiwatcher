""" to be merged in with nob/1 """

import __init__
from articlerevisions import ArticleRevisions

def test_format_timestamp():
    """ tests module level function for creating timestamp string from ints"""
    t_revisions = ArticleRevisions("test")
    # full datetime
    assert t_revisions.format_timestamp(2008, 6, 7, 4, 1, 30) == '20080607040130'
    # partials to do
    #assert a.format_timestamp(2008, 0, 7, 4, 1, 30) == '20080607040130'

if __name__ == "__main__":
    test_format_timestamp()
