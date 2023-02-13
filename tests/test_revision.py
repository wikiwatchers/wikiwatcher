'''Tests for class revision'''
import __init__
import json
import requests
from revision import Revision, URL, datetime
with open('tests/queries.json', 'r', encoding='utf-8') as q:
    TPARAMS = json.load(q)

# pylint: disable=W0603,W0602

T_REV = None

def test_revision_init():
    '''Tests initialization of a single example revision'''
    global T_REV, TPARAMS
    j = requests.get(URL, TPARAMS).json()
    revisionjson = j['query']['allrevisions'][0]['revisions'][0]
    revisionjson['pageid'] = j['query']['allrevisions'][0]['pageid']
    revisionjson['title'] = j['query']['allrevisions'][0]['title']
    T_REV = Revision(revisionjson)
    assert T_REV.comment == '"FMV\'s". See http://www.angryflower.com/aposter3.jpg'
    assert T_REV.minor
    assert T_REV.pageid == 7020642
    assert T_REV.parentid == 215441879
    assert T_REV.revid == 217678584
    assert T_REV.size == 5216
    assert T_REV.tags == []
    assert T_REV.timestamp == '2008-06-07T04:01:30Z'
    assert T_REV.title == 'Far Cry Vengeance'
    assert T_REV.user == 'Starfox'
    assert T_REV.userid == 396168

def test_get_content():
    '''Tests get_content method against known correct output'''
    global T_REV
    if T_REV is None:
        test_revision_init()
    page_content = T_REV.get_content()
    page_content = page_content[0:page_content.index('<!')] # remove variable mwparser cmt
    with open('tests/resources/revision-get_contents.html', 'r', encoding='utf-8') as in_file:
        f_content_l = list(in_file.readlines())
        f_content_l = f_content_l[0:57] # remove variable mwparser cmt
        f_content = ''.join(f_content_l)
        assert f_content == str(page_content)

def test_get_diff():
    '''Tests get_diff method against known correct output'''
    global T_REV
    if T_REV is None:
        test_revision_init()
    rev_diff = T_REV.get_diff()
    assert rev_diff is not None
    # get_diff should return json of changes
    #print(rev_diff)

def test_timestamp_to_datetime():
    '''Tests get_timestamp method against known correct output'''
    global T_REV
    if T_REV is None:
        test_revision_init()
    rev_datetime = T_REV.timestamp_to_datetime()
    assert rev_datetime == datetime(2008, 6, 7, 4, 1, 30)


if __name__ == '__main__':
    #print("run python -m pytest")
    test_get_diff()
