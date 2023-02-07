""" API/App.py
Defines endpoints of the API
Heavily WIP
"""
import requests as r
from flask import Flask
# from flask import request
app = Flask("WikiWatcher")


@app.route("/")
def index():
    """Temporary test code - may put a UI here at some point?"""
    return "Test Flask response"


# URLs for our endpoints should share similar patterns:
# /<x>History/<title/name>?fromdate=<fromdate>&todate=<>&keyword=<>&tag=<>
@app.route("/revisionHistory/<title>")
def get_revisions(title):
    """ /revisionHistory/TITLE?fromdate=_&todate=_&keyword=_&tag=_


    This is exploratory/prototype code which will likely be
    abstracted away into a RevisionHistory class.
    i.e. initiate a RevisionHistory with a title,
    RevisionHistory will have list attribute storing Revisions,
    as well as methods for initializing and/or filtering that list?
    query it using its methods for...
    """
    # construct target URL
    url = "https://api.wikimedia.org/core/v1/wikipedia/en/page/"\
        + "<title>/history".replace("<title>", title)
    # prepare to translate parameters
    # from_date = request.args.get("fromDate")
    # to_date = request.args.get("toDate")
    from_id = None
    to_id = None
    # match datetimes to IDs
    # processing_revisions = r.get(url=url, timeout=5)
    # for p_revision in processing_revisions.json()["revisions"]:
    # pass
    # if p_revision[]
    # prepare request to Wikimedia API
    params = {
        "older_than": to_id,
        "newer_than": from_id
    }
    for param in params.copy():  # Dict must not change during iteration
        if params[param] is None:
            params.pop(param)
    # send request to Wikimedia API
    revisions = r.get(url=url, params=params, timeout=5)
    # print(json.dumps(revisions.json(), indent=1))
    return revisions.json()["revisions"]


if __name__ == "__main__":
    app.run(debug=True)
