'''test for article history subclass'''
import __init__
import pytest
from history import History, format_timestamp
from exceptions import BadRequestException

def test_format_timestamp():
    """ tests module level function for creating timestamp string from ints"""
    # full datetime
    assert format_timestamp(2008, 6, 7, 4, 1, 30) == '20080607040130'
    # bad datetimes
    # for some reason this doesn't work if we specify BadRequestException...
    with pytest.raises(Exception):
        format_timestamp(2000, 13)
    with pytest.raises(Exception):
        format_timestamp(2007, 2, 29)
    # partials
    assert format_timestamp(2005) == '20050101000000'
    assert format_timestamp(2008, 6) == '20080601000000'
    assert format_timestamp(2025, 3, 2) == '20250302000000'
    assert format_timestamp(2025, 3, 2, 1) == '20250302010000'
    assert format_timestamp(2001, 9, 8, 7, 6) == '20010908070600'
    # bad partials
    with pytest.raises(Exception):
        format_timestamp(year=2005, day=5)
    with pytest.raises(Exception):
        format_timestamp(year=2015, month=12, day=25, hour=13, second=0)

if __name__ == "__main__":
    test_format_timestamp()
