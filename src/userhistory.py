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
        '''self.startyear = startyear
        self.startmonth = startmonth
        self.startday = startday
        self.starthour = starthour
        self.startminute = startminute
        self.startsecond = startsecond

        self.endyear = endyear
        self.endmonth = endmonth
        self.endday = endday
        self.endhour = endhour
        self.endminute = endminute
        self.endsecond = endsecond'''

        self.call_wikipedia_api()
        #filter here

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.user: str = None

    def call_wikipedia_api(self):
        ''' pulls down user's edit history from Wikipedia API '''
        self.revisions = []
        '''self.rvstart = format_timestamp(self.startyear, self.startmonth,
                                        self.startday, self.starthour,
                                        self.startminute, self.startsecond)
        self.rvend = format_timestamp(self.endyear, self.endmonth,
                                        self.endday, self.endhour,
                                        self.endminute, self.endsecond)'''
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
