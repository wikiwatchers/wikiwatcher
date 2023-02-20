""" app.py
Defines endpoints of our API
Handles interactions with our users, does not handle interactions with external APIs
"""
import __init__
import sys
import json
from flask import Flask, request
from markdown import markdown
from src.revision import URL
from src.userhistory import UserHistory
try:
    from src.articlehistory import ArticleHistory
except ModuleNotFoundError as modError:
    print(modError, "Waiting to merge")
try:
    from src.articlehistory import ArticleRevisions
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

@app.route("/articleHistory/<title>")
def get_article_history(title):
    """ /articleHistory/<title>?...
    Returns a JSON collection of revisions made to an article.
    Takes mandatory article title argument and optional parameters filtering for:
        tags,
        keyword (in content of revisions),
        username of editor,
        starting & ending year, month, day, hour, minute, and second
            to filter revisions by datetime
    """
    # gather user inputs
    tags: list[str] = parse_tags(request.args.get("tags", default=None, type=str))
    keyword: str = request.args.get("keyword", default=None, type=str)
    rvuser: str = request.args.get("user", default=None, type=str)
    startyear: int = request.args.get("startyear", default=None, type=int)
    startmonth: int = request.args.get("startmonth", default=None, type=int)
    startday: int = request.args.get("startday", default=None, type=int)
    starthour: int = request.args.get("starthour", default=None, type=int)
    startminute: int = request.args.get("startminute", default=None, type=int)
    startsecond: int = request.args.get("startsecond", default=None, type=int)
    endyear: int = request.args.get("endyear", default=None, type=int)
    endmonth: int = request.args.get("endmonth", default=None, type=int)
    endday: int = request.args.get("endday", default=None, type=int)
    endhour: int = request.args.get("endhour", default=None, type=int)
    endminute: int = request.args.get("endminute", default=None, type=int)
    endsecond: int = request.args.get("endsecond", default=None, type=int)
    # gather and filter revisions
    if "src.articlehistory" in sys.modules:
        revisions = ArticleHistory(titles=title,
                                     startyear=startyear, startmonth=startmonth, startday=startday,
                                     starthour=starthour, startminute=startminute,
                                     startsecond=startsecond, endyear=endyear, endmonth=endmonth,
                                     endday=endday, endhour=endhour, endminute=endminute,
                                     endsecond=endsecond, tags=tags, rvuser=rvuser, keyword=keyword)
        ret = json.dumps(revisions.revisions)
    else:
        ret = "-1" # placeholder
    return ret

@app.route("/userHistory/<username>")
def get_user_history(username):
    """ /userHistory/<username>?...
    Returns a JSON collection of revisions made by a user.
    Takes mandatory username argument and optional parameters filtering for:
        tags,
        keyword (in content of revisions),
        article title,
        starting & ending year, month, day, hour, minute, and second
            to filter revisions by datetime
    """
    # gather user inputs
    tags: list[str] = parse_tags(request.args.get("tags", default=None, type=str))
    keyword: str = request.args.get("keyword", default=None, type=str)
    titles: str = request.args.get("title", default=None, type=str)
    startyear: int = request.args.get("startyear", default=None, type=int)
    startmonth: int = request.args.get("startmonth", default=None, type=int)
    startday: int = request.args.get("startday", default=None, type=int)
    starthour: int = request.args.get("starthour", default=None, type=int)
    startminute: int = request.args.get("startminute", default=None, type=int)
    startsecond: int = request.args.get("startsecond", default=None, type=int)
    endyear: int = request.args.get("endyear", default=None, type=int)
    endmonth: int = request.args.get("endmonth", default=None, type=int)
    endday: int = request.args.get("endday", default=None, type=int)
    endhour: int = request.args.get("endhour", default=None, type=int)
    endminute: int = request.args.get("endminute", default=None, type=int)
    endsecond: int = request.args.get("endsecond", default=None, type=int)
    # gather and filter revisions
    if "src.userhistory" in sys.modules:
        revisions = UserHistory(user=username,
                                startyear=startyear, startmonth=startmonth, startday=startday,
                                starthour=starthour, startminute=startminute,
                                startsecond=startsecond, endyear=endyear, endmonth=endmonth,
                                endday=endday, endhour=endhour, endminute=endminute,
                                endsecond=endsecond, tags=tags, titles=titles, keyword=keyword)
        ret = json.dumps(revisions.revisions)
    else:
        ret = "-1" # placeholder
    return ret

@app.route("/getRevision/<title>")
def get_revision(title):
    """ /getRevision/<title>?...
    Returns the contents of a single revision.
    Takes a mandatory argument for article title, as well as
    a mandatory year parameter and optional month, day, hour, minute, and second
    """
    startyear: int = request.args.get("startyear", default=None, type=int)
    startmonth: int = request.args.get("startmonth", default=None, type=int)
    startday: int = request.args.get("startday", default=None, type=int)
    starthour: int = request.args.get("starthour", default=None, type=int)
    startminute: int = request.args.get("startminute", default=None, type=int)
    startsecond: int = request.args.get("startsecond", default=None, type=int)
    if "src.articlehistory" in sys.modules:
        revisions = ArticleHistory(titles=title,
                                   startyear=startyear, startmonth=startmonth,
                                   startday=startday, starthour=starthour,
                                   startminute=startminute, startsecond=startsecond)
        ret = json.dumps({"content": revisions.revisions[0].get_content()})
    else:
        ret = -1
    return ret

@app.route("/compareRevisions/<title>")
def get_difference(title):
    """ /getRevision/<title>?...
    Returns the difference between two revisions a and b.
    Takes a mandatory argument for article title, as well as
    a mandatory year parameter and optional month, day, hour, minute, and second
    for revision a, as well as
    a mandatory year parameter and optional month, day, hour, minute, and second
    for revision b.
    """
    startyear: int = request.args.get("startyear", default=None, type=int)
    startmonth: int = request.args.get("startmonth", default=None, type=int)
    startday: int = request.args.get("startday", default=None, type=int)
    starthour: int = request.args.get("starthour", default=None, type=int)
    startminute: int = request.args.get("startminute", default=None, type=int)
    startsecond: int = request.args.get("startsecond", default=None, type=int)
    endyear: int = request.args.get("endyear", default=None, type=int)
    endmonth: int = request.args.get("endmonth", default=None, type=int)
    endday: int = request.args.get("endday", default=None, type=int)
    endhour: int = request.args.get("endhour", default=None, type=int)
    endminute: int = request.args.get("endminute", default=None, type=int)
    endsecond: int = request.args.get("endsecond", default=None, type=int)
    if "src.articlehistory" in sys.modules:
        revisions = ArticleHistory(titles=title,
                                   startyear=startyear, startmonth=startmonth,
                                   startday=startday, starthour=starthour,
                                   startminute=startminute, startsecond=startsecond,
                                   endyear=endyear, endmonth=endmonth,
                                   endday=endday, endhour=endhour,
                                   endminute=endminute, endsecond=endsecond)
        ret = json.dumps({"diff":
            revisions.revisions[0].get_diff(revisions.revisions[-1].revid)
        })
    else:
        ret = -1
    return ret

if __name__ == "__main__":
    app.run(debug=True)
