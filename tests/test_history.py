"""test for article history subclass"""
import __init__
import pytest
import json
try:
    from src.history import History
    from src.exceptions import BadRequestException
    from src.revision import Revision
except ModuleNotFoundError:
    from history import History
    from exceptions import BadRequestException
    from revision import Revision

def test_get_list_of_revision_key_data():
    """tests get_list_of_revision_key_data"""
    with open("tests/resources/wikipedia_responses.json", "r", encoding="utf-8") as file:
        known_rev = file.read()
        response_json = json.loads(known_rev)["query"]
        known_rev_json = response_json["pages"][0]["revisions"][0]
        known_rev_json["title"] = response_json["pages"][0]["title"]
        known_rev_json["pageid"] = response_json["pages"][0]["pageid"]
    test_revision = Revision(known_rev_json)

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
