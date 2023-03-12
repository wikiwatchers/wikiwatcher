"""test for article history subclass"""
import __init__
import pytest
import json
try:
    from src.history import History, format_timestamp
    from src.exceptions import BadRequestException
    from src.revision import Revision
except ModuleNotFoundError:
    from history import History, format_timestamp
    from exceptions import BadRequestException
    from revision import Revision

def test_format_timestamp():
    """ tests module level function for creating timestamp string from ints"""
    # full datetime
    assert format_timestamp(2008, 6, 7, 4, 1, 30) == "20080607040130"
    # bad datetimes
    # for some reason this doesn't work if we specify BadRequestException...
    with pytest.raises(Exception):
        format_timestamp(2000, 13)
    with pytest.raises(Exception):
        format_timestamp(2007, 2, 29)
    # partials
    assert format_timestamp(2005) == "20050101000000"
    assert format_timestamp(2008, 6) == "20080601000000"
    assert format_timestamp(2025, 3, 2) == "20250302000000"
    assert format_timestamp(2025, 3, 2, 1) == "20250302010000"
    assert format_timestamp(2001, 9, 8, 7, 6) == "20010908070600"
    # bad partials
    with pytest.raises(Exception):
        format_timestamp(year=2005, day=5)
    with pytest.raises(Exception):
        format_timestamp(year=2015, month=12, day=25, hour=13, second=0)

def test_get_list_of_revision_key_data():
    """tests get_list_of_revision_key_data"""
    with open("tests/resources/wikipedia_responses.json", "r", encoding="utf-8") as file:
        known_response = file.read()
        response_json = json.loads(known_response)["query"]
        known_revision_json = response_json["pages"][0]["revisions"][0]
        known_revision_json["title"] = response_json["pages"][0]["title"]
        known_revision_json["pageid"] = response_json["pages"][0]["pageid"]
    test_revision = Revision(known_revision_json)

    rev_key_list = []
    for _ in range(10):
        rev_key_list.append(test_revision)

    history_test = History()
    history_test.revisions = rev_key_list

    rev_key_list_userid = []
    for each_rev in rev_key_list:
        rev_key_list_userid.append(each_rev.userid)

    assert history_test.get_list_of_revision_key_data("userid") == rev_key_list_userid

    rev_key_list_timestamp = []
    for each_rev in rev_key_list:
        rev_key_list_timestamp.append(each_rev.timestamp)

    assert history_test.get_list_of_revision_key_data("timestamp") == rev_key_list_timestamp

if __name__ == "__main__":
    test_format_timestamp()
