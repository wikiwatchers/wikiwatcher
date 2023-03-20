""" app.py
Defines endpoints of our API
Handles interactions with our users, does not handle interactions with external APIs
"""
import __init__
import io
import json
import dateutil.parser
from flask import Flask, render_template, request, Response, redirect
from flask_caching import Cache
from markdown import markdown
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from src.revision import URL
from src.exceptions import NoRevisionsException
from src.userhistory import UserHistory
from src.articlehistory import ArticleHistory
from src.exceptions import BadRequestException
from src.histogram import Histogram
from src.pie import Pie
from src.requests import add_params_to_url

app = Flask("WikiWatcher")
mem_cache = Cache(app, config={"CACHE-TYPE": "simple"})
CACHE_TIMEOUT = 120 # seconds

def validate_tagstring(tagstring):
    """ ensures user passed a list of tags to endpoint """
    # how should we handle bad input?
    assert tagstring[0] == "["
    assert tagstring[-1] == "]"

def parse_tags(tagstring):
    """ parses user tag string-list into python list """
    if tagstring is None:
        return None
    tagstring = tagstring[1:-1]
    return tagstring.split(",")

@app.route("/")
def index():
    """ Our index landing page """
    with open("README.md", "r", encoding="utf-8") as readme:
        content = markdown(readme.read())
    return render_template('index.html', content=content)

@app.route("/form")
def form():
    """ Form page """
    return render_template('form.html')

@app.route("/formrequest")
def formrequest():
    """ Route to handle form requests """
    base_url = "/"
    endpoint = request.args.get("endpoint")
    match endpoint:
        case "User History":
            base_url = add_params_to_url("userHistory/",
                                        request.args.get("user"),
                                        base_url, "?")
        case "Article History":
            base_url = add_params_to_url("articleHistory/",
                                        request.args.get("title"),
                                        base_url, "?")
        case "Compare Revisions":
            base_url = add_params_to_url("compareRevisions/",
                                        request.args.get("title"),
                                        base_url, "?")

    if request.args.get("keyword"):
        base_url = add_params_to_url("keyword=",
                                    request.args.get("keyword"),
                                    base_url, "&")

    if endpoint != "User History" and request.args.get("user"):
        base_url = add_params_to_url("user=",
                                    request.args.get("user"),
                                    base_url, "&")

    if endpoint == "User History" and request.args.get("title"):
        base_url = add_params_to_url("titles=",
                                    request.args.get("title"),
                                    base_url, "&")

    if request.args.get("startTime"):
        start_time = dateutil.parser.parse(request.args.get("startTime"))
        base_url = add_params_to_url("startYear=",
                                    str(start_time.year),
                                    base_url, "&")
        base_url = add_params_to_url("startMonth=",
                                    str(start_time.month),
                                    base_url, "&")
        base_url = add_params_to_url("startDay=",
                                    str(start_time.day),
                                    base_url, "&")
        base_url = add_params_to_url("startMinute=",
                                    str(start_time.minute),
                                    base_url, "&")
        base_url = add_params_to_url("startSecond=",
                                    str(start_time.second),
                                    base_url, "&")

    if request.args.get("endTime"):
        end_time = dateutil.parser.parse(request.args.get("endTime"))
        base_url = add_params_to_url("endYear=",
                                    str(end_time.year),
                                    base_url, "&")
        base_url = add_params_to_url("endMonth=",
                                    str(end_time.month),
                                    base_url, "&")
        base_url = add_params_to_url("endDay=",
                                    str(end_time.day),
                                    base_url, "&")
        base_url = add_params_to_url("endMinute=",
                                    str(end_time.minute),
                                    base_url, "&")
        base_url = add_params_to_url("endSecond=",
                                    str(end_time.second),
                                    base_url, "&")

    if request.args.get("tags"):
        tags = "[" + request.args.get("tags") + "]"
        base_url = add_params_to_url("tags=", tags, base_url, "&")

    if request.args.get("visualize") and request.args.get("visualize") != "":
        base_url = add_params_to_url("visualize=", request.args.get("visualize"), base_url, "")

    return redirect(base_url)

@app.route("/articleHistory/<title>")
@mem_cache.cached(timeout=CACHE_TIMEOUT)
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
    user: str = request.args.get("user", default=None, type=str)
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
    visualize: str = request.args.get("visualize", default=None, type=str)
    # gather and filter revisions
    try:
        revisions = ArticleHistory(titles=title,
                                   startyear=startyear, startmonth=startmonth, startday=startday,
                                   starthour=starthour, startminute=startminute,
                                   startsecond=startsecond, endyear=endyear, endmonth=endmonth,
                                   endday=endday, endhour=endhour, endminute=endminute,
                                   endsecond=endsecond, tags=tags, user=user, keyword=keyword)
        # https://stackoverflow.com/questions/50728328/
        # python-how-to-show-matplotlib-in-flask/50728936#50728936
        if visualize:
            output = io.BytesIO()
            chart = None
            match visualize:
                case "revisions_per_time":
                    chart = Histogram(revisions)
                case "revisions_per_user":
                    chart = Pie(revisions)
                case _:
                    raise BadRequestException("Invalid choice of visualization")
            FigureCanvas(chart.graph).print_png(output)
            return Response(output.getvalue(), mimetype="image/png")
        return revisions.revisions_as_json()
    except BadRequestException as bre:
        return "<h1>Bad Request</h1>" + str(bre), 400
    except NoRevisionsException as nre:
        return "<h1>No Revisions</h1>" + str(nre), 404

@app.route("/userHistory/<username>")
@mem_cache.cached(timeout=CACHE_TIMEOUT)
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
    # temporarily disabling some pylint errors while waiting for class userhistory
    #pylint: disable=E1123,E1120
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
    visualize: str = request.args.get("visualize", default=None, type=str)
    # gather and filter revisions
    try:
        revisions = UserHistory(user=username,
                                startyear=startyear, startmonth=startmonth, startday=startday,
                                starthour=starthour, startminute=startminute,
                                startsecond=startsecond, endyear=endyear, endmonth=endmonth,
                                endday=endday, endhour=endhour, endminute=endminute,
                                endsecond=endsecond, tags=tags, titles=titles, keyword=keyword)
        # https://stackoverflow.com/questions/50728328/
        # python-how-to-show-matplotlib-in-flask/50728936#50728936
        if visualize:
            output = io.BytesIO()
            chart = None
            match visualize:
                case "revisions_per_time":
                    chart = Histogram(revisions)
                case "revisions_per_article":
                    chart = Pie(revisions)
                case _:
                    raise BadRequestException("Invalid choice of visualization")
            FigureCanvas(chart.graph).print_png(output)
            return Response(output.getvalue(), mimetype="image/png")
        return revisions.revisions_as_json()
    except BadRequestException as bre:
        return "<h1>Bad Request</h1>" + str(bre), 400
    except NoRevisionsException as nre:
        return "<h1>No Revisions</h1>" + str(nre), 404

@app.route("/getRevision/<title>")
@mem_cache.cached(timeout=CACHE_TIMEOUT)
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
    try:
        revisions = ArticleHistory(titles=title,
                                    startyear=startyear, startmonth=startmonth,
                                    startday=startday, starthour=starthour,
                                    startminute=startminute, startsecond=startsecond)
        ret = json.dumps(revisions.revisions[0].get_content())
        return ret
    except BadRequestException as bre:
        return "<h1>Bad Request</h1>" + str(bre), 400
    except NoRevisionsException as nre:
        return "<h1>No Revisions</h1>" + str(nre), 404

@app.route("/compareRevisions/<title>")
@mem_cache.cached(timeout=CACHE_TIMEOUT*2)
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
    visualize: str = request.args.get("visualize", default=None, type=str)
    try:
        revisions = ArticleHistory(titles=title,
                                    startyear=startyear, startmonth=startmonth,
                                    startday=startday, starthour=starthour,
                                    startminute=startminute, startsecond=startsecond,
                                    endyear=endyear, endmonth=endmonth,
                                    endday=endday, endhour=endhour,
                                    endminute=endminute, endsecond=endsecond)
        ret = json.dumps(revisions.revisions[0].get_diff(revisions.revisions[-1].revid))
        formatted_output = ret.replace('\\n', '\n').replace('\\t', '\t')

        if visualize:
            match visualize:
                case "side_by_side":
                    first_article = revisions.revisions[0].get_content()
                    second_article = revisions.revisions[-1].get_content()
                    first_date = revisions.revisions[0].timestamp
                    second_date = revisions.revisions[-1].timestamp
                    return render_template('comparison.html',
                                           title=title,
                                           first_article=first_article,
                                           second_article=second_article,
                                           first_date=first_date,
                                           second_date=second_date)
                case _:
                    raise BadRequestException("Invalid choice of visualization")

        return formatted_output
    except BadRequestException as bre:
        return "<h1>Bad Request</h1>" + str(bre), 400
    except NoRevisionsException as nre:
        return "<h1>No Revisions</h1>" + str(nre), 404


if __name__ == "__main__":
    app.run(debug=True)
