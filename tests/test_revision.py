"""Tests for class revision"""
import __init__
import json
import requests
from revision import Revision, URL, datetime

def test_revision_init():
    """Tests initialization of a single revision
    mocks behavior to be implemented in collection classes """
    with open("tests/resources/wikipedia_responses.json", "r", encoding="utf-8") as file:
        known_response = file.read()
        response_json = json.loads(known_response)["query"]
        known_revision_json = response_json["pages"][0]["revisions"][0]
        known_revision_json["title"] = response_json["pages"][0]["title"]
        known_revision_json["pageid"] = response_json["pages"][0]["pageid"]
    test_revision = Revision(known_revision_json)
    assert not test_revision.minor
    assert test_revision.comment == "add peak"
    assert test_revision.pageid == 61495838
    assert test_revision.parentid == 1126322774
    assert test_revision.revid == 1127195995
    assert test_revision.size == 63658
    assert test_revision.tags == ["wikieditor"]
    assert test_revision.timestamp == "2022-12-13T11:41:23Z"
    assert test_revision.title == "100 Gecs"
    assert test_revision.user == "Ss112"
    assert test_revision.userid == 1286970


def test_contains_tag():
    """tests contain tag function inside revision class"""
    test_revision = Revision({})
    test_revision.tags = ["Reverted", "wikieditor"]
    assert test_revision.contains_tag(["Reverted"]) is True
    test_revision.tags = []
    assert test_revision.contains_tag(["Reverted"]) is False
    assert test_revision.contains_tag([""]) is False
    test_revision.tags.append("wikieditor")
    assert test_revision.contains_tag(["wikieditor"]) is True
    assert test_revision.contains_tag(["wikieditor", "somethingelse"]) is False
    test_revision.tags.append("Techno")
    test_revision.tags.append("somethingelse")
    assert test_revision.contains_tag(["wikieditor", "somethingelse"]) is True
    test_revision.tags = []
    assert test_revision.contains_tag(["wikieditor", "somethingelse"]) is False


def test_get_content():
    """ Tests get_content method against known correct output """
    test_revision = Revision({})
    test_revision.revid = 739873
    content = test_revision.get_content()
    content = content[0:content.index("<!")]  # remove variable mwparser cmt
    content = content.replace("\r", "r")
    content = content.replace("\'", "'")
    with open("tests/resources/revision-get_contents.html", "r", encoding="utf-8") as in_file:
        f_content = "".join(in_file.readlines())
        assert f_content == content


def test_get_diff():
    """Tests get_diff method against known correct output"""
    test_revision = Revision({})
    test_revision.revid = 1127195995
    test_revision.parentid = 1126322774
    diff = test_revision.get_diff()
    diff = diff[0:diff.index("<!-")]  # remove variable timestamp cmt
    with open("tests/resources/revision-get_diff.html", "r", encoding="utf-8") as in_file:
        f_diff = "".join(in_file.readlines())
        assert f_diff == diff

if __name__ == "__main__":
    # print("run python -m pytest")
    test_get_content()
