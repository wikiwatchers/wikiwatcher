from datetime import datetime
import requests
import json


class User():
    def __init__(self, name: str, id: int) -> None:
        self.name: str = name
        self.id: int = id


class Revision():
    def __init__(self) -> None:
        # possible params
        self.json: dict = None
        self.id: int = None
        self.title: str = None
        self.timestamp: datetime = None
        self.pageId: int = None
        self.user: User = None
        self.minor: bool = None
        self.tags: list[str] = None
        self.comment: str = None
        self.parentId: int = None
        # present in Pagehistory but not Usercontribs
        self.size: int = None

    def assign_contents(self, pages):

        revisions = pages["revisions"][0]

        self.json = pages
        self.id = revisions["revid"]
        self.title = pages["title"]
        self.timestamp = revisions["timestamp"]
        self.pageId = pages["pageid"]
        self.user = User(revisions["user"], revisions["userid"])
        self.minor = revisions["minor"]
        self.tags = revisions["tags"]
        self.parentId = revisions["parentid"]
        self.size = revisions["size"]
        self.comment = revisions["comment"]


    def get_contents(self, title):
        """ Returns the content of the page at this revision
        Hits mediawiki.org API with
        "action": "query",
        "prop": "revisions",
        "rvprop": "content"
        """

        S = requests.Session()

        URL = "https://www.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "prop": "revisions",
            "titles": title,
            "rvprop": "timestamp|user|userid|comment|content|tags|ids|size|flags",
            "rvslots": "main",
            "formatversion": "2",
            "format": "json",
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        PAGES = DATA["query"]["pages"]

        #assign contents of PAGES to the object
        self.assign_contents(PAGES[0])

        #print(json.dumps(PAGES, indent=1))





    def get_diff(self, toId: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """
        if toId is None:  # compare with parent
            if self.parentId is None:  # articleHistory, handle elsewhere?
                pass  # raise an exception to be caught in articleHistory? TODO
            else:  # userHistory, handle here
                pass  # TODO
        else:  # compare self to toid, hit getrevision endpoint
            pass  # TODO
