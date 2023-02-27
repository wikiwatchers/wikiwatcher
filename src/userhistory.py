'''defines user history class'''
import datetime
import requests
from src.revision import Revision, URL
from src.history import format_timestamp,History
from src.exceptions import BadRequestException
import mwparserfromhell as mwp

class UserHistory(History):
    ''' UserHistory object parses json user contributions '''
    def __init__(self, user, startyear=None, startmonth=None, startday=None,
                starthour=None, startminute=None, startsecond=None,
                endyear=None, endmonth=None, endday=None, endhour=None,
                endminute=None, endsecond=None, tags=None, titles=None, keyword=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(titles, user, keyword, tags, startyear, startmonth, startday,
                         starthour, startminute, startsecond,endyear, endmonth, endday,
                         endhour, endminute, endsecond)

        self.call_wikipedia_api()
        self.filter()

    def init_to_none(self):
        ''' Sets up class data members and initializes them to None '''
        self.user: str = None

    def call_wikipedia_api(self):
        ''' Pulls down user's edit history from Wikipedia API '''
        self.revisions = []
        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucprop": "comment|ids|flags|size|tags|timestamp|user|userid",
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
