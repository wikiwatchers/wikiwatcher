from Revision import Revision, User
from datetime import datetime
import requests

class ArticleRevisions(self, titles, user, keyword, tags[], rvstart, rvend=None):
    def __init__(self):
        self.init_to_none()
        self.titles = titles
        self.user = user
        self.keyword = keyword
        self.tags[] = tags[]

        format_timestamp()
        self.rvstart = rvstart
        self.rvend = rvend #if None, pull single revision from rvstart
        self.revisions: list[Revision] = None
        
        #call api
        #parse into revisions objects
        #filter

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.titles: string = None
        self.user: str = None
        self.keyword: str = None
        self.tags: list[str] = None
        self.rvstart: datetime = None
        self.rvend: datetime = None
        self.revisions: list[Revision] = None

    def format_timestamp():
        pass

    def filter(self, user, keyword, tags[], rvstart, rvend=None):
        pass
    
    def get_article_revisions(self):
        '''pulls down an article's revision history from the API'''

        session = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "prop": "revisions",
            "titles": self.titles,
            "arvprop": "comment|ids|flags|size|timestamp|user|userid",
            "arvuser": "Place holder",
            "list": "allrevisions",
            "format": "json"
        }

        rev = session.get(url=URL, params=PARAMS)
        data = rev.json()

        all_revisions = data["query"]["allrevisions"]

        for rev in all_revisions:
            print(rev)

        
