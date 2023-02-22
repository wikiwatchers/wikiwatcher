'''test for article history subclass'''
import __init__
import pytest
from history import History, format_timestamp

def test_format_timestamp():
    """ tests module level function for creating timestamp string from ints"""
    # full datetime
    assert format_timestamp(2008, 6, 7, 4, 1, 30) == '20080607040130'
    # partials
    assert format_timestamp(2008, 6) == '20080601000001'

if __name__ == "__main__":
    test_format_timestamp()
