""" API/App.py
Defines endpoints of the API
temporary/early version for setting up CI/CD
"""
import requests as r
from flask import Flask
app = Flask("WikiWatcher")


@app.route("/")
def index():
    """Temporary test code - may put a UI here at some point?"""
    return "Test Flask response"


@app.route("/revisionHistory/<title>")
def get_revisions(title):
    """
    Returns a JSON object containing the 20 most recent 
    revision objects to the article specified by <title>

    This is exploratory/prototype code which will likely be
    abstracted away into a RevisionHistory class.
    """
    url = "https://api.wikimedia.org/core/v1/wikipedia/en/page/"\
        + "<title>/history".replace("<title>", title)
    revisions = r.get(url=url, timeout=5)
    # print(json.dumps(revisions.json(), indent=1))
    return revisions.json()["revisions"]


if __name__ == "__main__":
    app.run(debug=True)
