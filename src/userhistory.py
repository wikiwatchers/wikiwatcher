'''defines user history class'''
import datetime
import requests
from src.revision import Revision, URL
from src.history import format_timestamp,History
from src.exceptions import BadRequestException
import mwparserfromhell as mwp

class UserHistory(History):
    '''userhistory object parses json user contributions '''
    def __init__(self, user, startyear=None, startmonth=None, startday=None,
                starthour=None, startminute=None, startsecond=None,
                endyear=None, endmonth=None, endday=None, endhour=None,
                endminute=None, endsecond=None, tags=None, titles=None, keyword=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(user, startyear, startmonth, startday,
                        starthour, startminute, startsecond,
                        endyear, endmonth, endday, endhour,
                        endminute, endsecond, tags, titles, keyword)

        self.user = user

        self.call_wikipedia_api()
        self.filter()

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.user: str = None

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
        ''' pulls down user's edit history from Wikipedia API '''
        self.revisions = []
        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": self.user,
            "ucstart": self.rvstart,
            "ucend" : self.rvend
        } | self.base_params
        if self.user is None:
            raise BadRequestException("User name missing")
        if self.rvstart is None:
            params["rvlimit"] = "10"

        request = session.get(url=URL, params=params)
        data = request.json()

        try:
            self.json = data['query']['usercontribs']
            for each_revision in self.json:
                self.revisions.append(Revision(each_revision))
        except BadRequestException:
            print("Data not found")

        return str(mwp.parse(data))
