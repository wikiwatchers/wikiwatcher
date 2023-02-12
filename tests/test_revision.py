import __init__
import json
import requests
from revision import Revision, URL
with open('tests/queries.json', 'r') as q:
    tparams = json.load(q)

T_REV = None

def test_revision_init():
    global T_REV
    j = requests.get(URL, tparams).json()
    revisionjson = j['query']['allrevisions'][0]['revisions'][0]
    revisionjson['pageid'] = j['query']['allrevisions'][0]['pageid']
    revisionjson['title'] = j['query']['allrevisions'][0]['title']
    T_REV = Revision(revisionjson)
    # TODO: assertions

def test_get_contents():
    global T_REV
    if T_REV is None:
        test_revision_init()
    page_content = T_REV.get_contents()
    with open('tests/resources/revision-get_contents.html') as f:
        //TODO: Test this
        f_content = str([line for line in f.readlines()])
        assert(f.read() == page_content)

if __name__ == '__main__':
    test_get_contents()