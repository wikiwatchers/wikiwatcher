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
        # present in Pagehistory but not userContribs
        self.size: int = None





    def get_contents(self, title='None', username='None'): #start and end time stamps???
        #Returns the content of the page at this revision

        S = requests.Session()

        URL = "https://www.wikipedia.org/w/api.php"

        PARAMS = {
            #params for Revisions API
            #https://www.mediawiki.org/wiki/API:Revisions
            "action": "query",
            "prop": "revisions",
            "titles": title,
            "rvprop": "comment|content|flags|ids|size|tags|timestamp|user|userid",
            "rvslots": "main",
            "formatversion": "2",
            "format": "json",
            #params for AllRevisions API
            #https://www.mediawiki.org/wiki/API:Allrevisions
            "arvuser": username,
            "arvprop": "comment|flags|ids|size|tags|timestamp|user|userid",
            "list": "allrevisions"

        }

        R = S.get(url=URL, params=PARAMS)
        data = R.json()

        if(title != 'None'):
            pageRevisions = data["query"]["pages"]
            self.json = pageRevisions[0] #first revision in the list
            print(json.dumps(self.json, indent=1))

        else:
            userRevisions = data["query"]["allrevisions"]
            self.json = userRevisions[0] #first revision in the list
            print(json.dumps(self.json, indent=1))


    def get_diff(self, toId: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """

        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
            'action':"compare",
            'format':"json",
            'fromtitle':'Template:Unsigned',
            'totitle':'Template:UnsignedIP'
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        print(DATA)
        """
        if toId is None:  # compare with parent
            if self.parentId is None:  # articleHistory, handle elsewhere?
                pass  # raise an exception to be caught in articleHistory? TODO
            else:  # userHistory, handle here
                pass  # TODO
        else:  # compare self to toid, hit getrevision endpoint
            pass  # TODO
            """
