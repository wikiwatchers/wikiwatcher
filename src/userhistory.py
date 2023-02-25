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
        #filter here

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.user: str = None

    def call_wikipedia_api(self):
        ''' pulls down user's edit history from Wikipedia API '''
        self.revisions = []
        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": self.user
        } | self.base_params
        if self.user is None:
            raise BadRequestException("User name missing")

        request = session.get(url=URL, params=params)

        data = request.json()['query']['usercontribs']

        try:
            self.json = data
            for revision in self.json:
                self.revisions.append(revision)
        except BadRequestException:
            print("Data not found")

        return str(mwp.parse(data))
