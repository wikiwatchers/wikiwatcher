'''defines revision base class'''
from datetime import datetime
import json
import requests
import mwparserfromhell as mwp

URL = "https://www.wikipedia.org/w/api.php"

# pylint: disable=R0902
class Revision():
    '''revision object parses json revision info into consistent '''

    def __init__(self, initjson: dict) -> None:
        # possible params
        self.json: dict = initjson
        self.init_to_none()
        attrs: list[str] = [key for key in vars(self).keys() if key != 'json']
        for attr in attrs:
            try:
                vars(self)[attr] = self.json[attr]
            except Exception as e:
                print(e) # TODO: do something more useful (log?)

    def init_to_none(self):
        self.pageid: int = None
        self.title: str = None
        self.revid: int = None
        self.parentid: int = None
        self.minor: bool = None
        self.user: jtr = None
        self.userid: int = None
        self.timestamp: datetime = None
        self.size: int = None
        self.comment: str = None
        self.tags: list[str] = None

    def get_contents(self):  # start and end time stamps???
        ''' Returns the content of the page at this revision'''

        session = requests.Session()

        params = {
            "action": "parse",
            "format": "json",
            "oldid": self.revid,
            "prop": "text",
        }
        if self.revid is not None:
            request = session.get(url=URL, params=params)
        else:
            raise Exception("Revision ID missing")
        data = request.json()['parse']['text']['*']
        return mwp.parse(data)

    def check_to_id(self, to_id):
        '''returns fromrev and torev args to parameters in get_diff'''
        if to_id is None:
            return self.revid, self.parentid
        return self.revid, to_id

    def get_diff(self, to_id: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """
        session = requests.Session()

        fromrev, torev = self.check_to_id(to_id)

        params = {
            # params for Compare API
            # https://www.mediawiki.org/wiki/API:Compare
            'action': "compare",
            'format': "json",
            'fromtitle': self.title,
            'totitle': self.title,
            'fromrev': fromrev,
            'torev': torev
        }

        request = session.get(url=URL, params=params)
        data = request.json()

        print(data)
