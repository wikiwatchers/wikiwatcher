from Revision import Revision, User
from datetime import datetime

class ArticleRevisions(self, titles, tags[], rvstart, rvend=None):
    def __init__(self):
        self.init_to_none()
        self.titles = titles
        self.tags[] = tags[]
        self.rvstart = rvstart
        self.rvend = rvend #if None, pull single revision from rvstart
        self.revisions: list[Revision] = None

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.revisions: list[Revision] = None
        self.titles: string = None
        self.tags: list[str] = None
        self.rvstart: datetime = None
        self.rvend: datetime = None
        self.revisions: list[Revision] = None

    def filter_by_timestamp(self):
        pass

    def filter_by_keyword(self, keyword):
        '''filters revisions by keyword'''
        pass

    def filter_by_tags(self, tags[]): #list of strings
        '''filters revisions by tags'''
        pass
    
    def get_article_revisions(self):
        '''pulls down an article's revision history from the API'''
        import requests

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
