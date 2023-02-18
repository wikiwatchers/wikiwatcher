""" app.py
Defines endpoints of our API
Handles interactions with our users, does not handle interactions with external APIs
"""
import __init__
import sys
from flask import Flask, request
from markdown import markdown
from src.revision import URL
from src.userrevisions import UserRevisions
try:
    from src.articlerevisions import ArticleRevisions
except ModuleNotFoundError as modError:
    print(modError, "Waiting to merge")
#import src.articlerevisions
app = Flask("WikiWatcher")

def validate_tagstring(tagstring):
    """ ensures user passed a list of tags to endpoint """
    # how should we handle bad input?
    assert tagstring[0] == "["
    assert tagstring[-1] == "]"

def parse_tags(tagstring):
    """ parses user tag string-list into python list """
    tagstring = tagstring[1:-1]
    return tagstring.split(",")

@app.route("/")
def index():
    """display readme for now - may put a GUI here later on"""
    with open("README.md", "r", encoding="utf-8") as readme:
        ret = markdown(readme.read())
    return ret

@app.route("/articleRevisions/<title>")
def get_article_revisions(title):
    """ /revisionHistory/<title>?... """
    # gather user inputs
    tags: list[str] = parse_tags(request.args.get("tags", default=None, type=str))
    keyword: str = request.args.get("keyword", default=None, type=str)
    user: str = request.args.get("user", default=None, type=str)
    # gather and filter revisions
    if "src.articlerevisions" in sys.modules:
        revisions = ArticleRevisions(titles=title,
                                     startyear=startyear, startmonth=startmonth, startday=startday,
                                     starthour=starthour, startminute=startminute, startsecond=startsecond,
                                     endyear=endyear, endmonth=endmonth, endday=endday,
                                     endhour=endhour, endminute=endminute, endsecond=endsecond,
                                     tags=tags, user=user, keyword=keyword)
    else:
        ret = "-1" # placeholder - we should discuss what to do in this case?

    return ret

@app.route("/userRevisions/<username>")
def get_user_revisions(username):
    """ /revisionHistory/<username>?fromdate=<>&todate=<>&keyword=<>&tags=<>&keyword=<> """
    return username # to do

if __name__ == "__main__":
    app.run(debug=True)
