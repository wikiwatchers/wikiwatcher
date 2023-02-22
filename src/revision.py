'''defines revision base class'''
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import mwparserfromhell as mwp

URL = "https://www.wikipedia.org/w/api.php"

class Revision():
    '''revision object parses json revision info into consistent '''

    def __init__(self, initjson: dict) -> None:
        self.json: dict = initjson
        self.init_to_none()
        for attr in [key for key in vars(self).keys() if key != 'json']:
            try:
                vars(self)[attr] = self.json[attr]
            except KeyError as err:
                print(err) # do something more useful? (log?)

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.pageid: int = None
        self.title: str = None
        self.revid: int = None
        self.parentid: int = None
        self.minor: bool = None
        self.user: str = None
        self.userid: int = None
        self.timestamp: str = None
        self.size: int = None
        self.comment: str = None
        self.tags: list[str] = None

    def get_content(self):  # start and end time stamps???
        ''' Returns the content of the page at this revision'''

        session = requests.Session()

        params = {
            "action": "parse",
            "format": "json",
            "oldid": self.revid,
            "prop": "text",
        }
        if self.revid is None:
            raise AttributeError("Revision ID missing")
        request = session.get(url=URL, params=params, timeout=5)
        data = request.json()['parse']['text']['*']
        ret = mwp.parse(data)
        return str(''.join(ret).replace("\n", ""))

    def get_diff(self, to_id: int = None):
        ''' Returns the difference between this revision and its parent
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        '''
        if to_id is None:
            if self.parentid is None:
                raise AttributeError("Revision parent ID missing")
            to_id = self.parentid
        session = requests.Session()
        params = {
            # params for Compare API
            # https://www.mediawiki.org/wiki/API:Compare
            'action': "compare",
            'format': "json",
            'fromtitle': self.title,
            'totitle': self.title,
            'fromrev': self.revid,
            'torev': to_id
        }
        wp_response = session.get(url=URL, params=params).json()
        # Can we return something more user-friendly?
        # Automatically color ins and del tags?
        return str(bs(wp_response['compare']['*'], features='lxml'))

    def timestamp_to_datetime(self):
        '''Converts the timestamp into a python-friendly datetime object
        for use in collections of revisions
        '''
        if self.timestamp is None:
            raise AttributeError("Revision timestamp missing")
        year = int(self.timestamp[0:4])
        month = int(self.timestamp[5:7])
        day = int(self.timestamp[8:10])
        hour = int(self.timestamp[11:13])
        minute = int(self.timestamp[14:16])
        second = int(self.timestamp[17:19])
        ret = datetime(year, month, day, hour, minute, second)
        return ret
