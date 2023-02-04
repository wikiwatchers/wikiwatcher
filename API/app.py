import requests as r
from flask import Flask
app = Flask("WikiWatcher")

@app.route("/")
def index():
	return "Test Flask response"

@app.route("/revisionHistory/<title>")
def get_revisions(title):
	# This will be abstracted away into a RevisionHistory class
	url = "https://api.wikimedia.org/core/v1/wikipedia/en/page/<title>/history".replace("<title>", title)
	revisions = r.get(url=url)
	#print(json.dumps(revisions.json(), indent=1))
	return revisions.json()["revisions"]

if __name__ == "__main__":
	app.run(debug=True)