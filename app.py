""" app.py
Defines endpoints of our API
Handles interactions with our users, does not handle interactions with external APIs
"""
import __init__
import sys
from flask import Flask, request
from markdown import markdown
from src.revision import URL
from src.userhistory import UserHistory
from src.articlehistory import ArticleHistory
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
    """ /articleHistory/<title>?... """
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
        revisions = ArticleRevisions(titles=title,
                                     startyear=startyear, startmonth=startmonth, startday=startday,
                                     starthour=starthour, startminute=startminute, startsecond=startsecond,
                                     endyear=endyear, endmonth=endmonth, endday=endday,
                                     endhour=endhour, endminute=endminute, endsecond=endsecond,
                                     tags=tags, rvuser=rvuser, keyword=keyword)
    else:
        ret = "-1" # placeholder - we should discuss what to do in this case?

    return ret

@app.route("/userHistory/<username>")
def get_user_revisions(username):
    """ /userHistory/<username>?... """
    # gather user inputs
    tags: list[str] = parse_tags(request.args.get("tags", default=None, type=str))
    keyword: str = request.args.get("keyword", default=None, type=str)
    title: str = request.args.get("user", default=None, type=str)
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
                                starthour=starthour, startminute=startminute, startsecond=startsecond,
                                endyear=endyear, endmonth=endmonth, endday=endday,
                                endhour=endhour, endminute=endminute, endsecond=endsecond,
                                tags=tags, rvuser=username, keyword=keyword)
    else:
        ret = "-1" # placeholder - we should discuss what to do in this case?
    return ret

if __name__ == "__main__":
    app.run(debug=True)
