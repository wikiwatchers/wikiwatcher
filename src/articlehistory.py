'''defines the collection class for article history'''
import requests
from datetime import datetime
from src.revision import Revision, URL
from src.history import format_timestamp, History

class ArticleHistory(History):
    '''article revision collection class'''

    def __init__(self, titles, user=None, keyword=None, tags=None,
                 startyear=None, startmonth=None, startday=None,
                 starthour=None, startminute=None, startsecond=None,
                 endyear=None, endmonth=None, endday=None, endhour=None,
                 endminute=None, endsecond=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(titles, user, keyword, tags,
                         startyear, startmonth, startday,
                         starthour, startminute, startsecond,
                         endyear, endmonth, endday,
                         endhour, endminute, endsecond)

        self.call_wikipedia_api()
        self.filter()

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.pageid: int = None

    def filter_by_keyword(self):
        '''filters list of revisions by keyword'''
        for rev in self.revisions.copy():
            if rev.contains_keyword(self.keyword) is False:
                self.revisions.remove(rev)

    def filter_by_tags(self):
        '''filters list of revisions by tags'''
        for rev in self.revisions.copy():
            if rev.contains_tag(self.tags) is False:
                self.revisions.remove(rev)

    def filter(self):
        '''calls filter helper functions'''
        if self.tags is not None:
            self.filter_by_tags()
        if self.keyword is not None:
            self.filter_by_keyword()

        if len(self.revisions) == 0:
            # throw exception instead??
            print("No revisions found matching your search parameters")

        # for each_revision in self.revisions:
        #    print(each_revision.json)

    def call_wikipedia_api(self):
        '''pulls down an article's revision history from the API'''
        self.revisions = []
        session = requests.Session()

        params = {
            "prop": "revisions",
            "titles": self.titles,
            "rvprop": "comment|ids|flags|size|tags|timestamp|user|userid",
            "formatversion": "2",
            "rvuser": self.user,
            "rvstart": self.rvstart,
            "rvend": self.rvend,

        } | self.base_params
        if self.rvstart is None:
            params["rvlimit"] = "10"

        rev = session.get(url=URL, params=params)
        data = rev.json()

        try:
            pages = data["query"]["pages"]
            self.json = pages[0]
            self.pageid = self.json["pageid"]
            for each_revision in self.json["revisions"]:
                each_revision["pageid"] = self.pageid
                each_revision["title"] = self.titles
                self.revisions.append(Revision(each_revision))

        except KeyError:
            print("Error accessing API with given parameters")
