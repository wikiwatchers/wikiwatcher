#from datetime import datetime
import json
import requests



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
        self.page_id: int = None
        self.user: User = None
        self.minor: bool = None
        self.tags: list[str] = None
        self.comment: str = None
        self.parent_id: int = None
        # present in Pagehistory but not userContribs
        self.size: int = None





    def get_contents(self, title='None', username='None'): #start and end time stamps???
        #Returns the content of the page at this revision

        s = requests.Session()

        url = "https://www.wikipedia.org/w/api.php"

        params = {
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

        r = s.get(url=url, params=params)
        data = r.json()

        if title != 'None':
            page_revisions = data["query"]["pages"]
            self.json = page_revisions[0] #first revision in the list
            print(json.dumps(self.json, indent=1))

        else:
            user_revisions = data["query"]["allrevisions"]
            self.json = user_revisions[0] #first revision in the list
            print(json.dumps(self.json, indent=1))


    def get_diff(self, to_id: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """

        s = requests.Session()

        url = "https://en.wikipedia.org/w/api.php"

        params = {
            'action':"compare",
            'format':"json",
            'fromtitle':'Template:Unsigned',
            'totitle':'Template:UnsignedIP'
        }

        r = s.get(url=url, params=params)
        data = r.json()

        print(data)
        """
        if toId is None:  # compare with parent
            if self.parentId is None:  # articleHistory, handle elsewhere?
                pass  # raise an exception to be caught in articleHistory? TODO
            else:  # userHistory, handle here
                pass  # TODO
        else:  # compare self to toid, hit getrevision endpoint
            pass  # TODO
            """
