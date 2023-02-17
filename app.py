""" API/App.py
Defines endpoints of the API
Heavily WIP
"""
import __init__
import sys
from flask import Flask
from markdown import markdown
from flask import request
from src.revision import URL
from src.userrevisions import UserRevisions
try:
    from src.articlerevisions import ArticleRevisions
except ModuleNotFoundError as modError:
    print(modError, "Waiting to merge")
#import src.articlerevisions
app = Flask("WikiWatcher")

def validate_tagstring(tagstring):
    # how should we handle bad input?
    assert tagstring[0] == "["
    assert tagstring[-1] == "]"

def parse_tags(tagstring):
    tagstring = tagstring[1:-1]
    return tagstring.split(",")

@app.route("/")
def index():
    """display readme for now - may put a GUI here later on"""
    with open("README.md", "r") as readme:
        ret = markdown(readme.read())
    return ret

@app.route("/revisionHistory/<title>")
def get_revisions(title):
    """ /revisionHistory/<title>?fromdate=<>&todate=<>&keyword=<>&tags=<>&keyword=<> """
    # gather user inputs
    rvstart: str = request.args.get("fromDate", type=str)
    rvend: str = request.args.get("toDate", default=None, type=str)
    tags: list[str] = parse_tags(request.args.get("tags", default=None, type=str))
    keyword: str = request.args.get("keyword", default=None, type=str)
    # gather and filter revisions
    if "src.articlerevisions" in sys.modules:
        revisions = ArticleRevisions(title, rvstart, rvend, tags)
        if tags:
            revisions.filter_by_tags(tags)
        if keyword:
            revisions.filter_by_keyword(keyword)
        ret = revisions
    else:
        ret = "-1" # placeholder - we should discuss what to do in this case?
    
    return ret

@app.route("/userRevisions/<username>")
def get_user_revisions(username):
    """ /revisionHistory/<username>?fromdate=<>&todate=<>&keyword=<>&tags=<>&keyword=<> """
    pass

if __name__ == "__main__":
    app.run(debug=True)
