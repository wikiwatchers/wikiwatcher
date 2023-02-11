'''defines revision base class'''
from datetime import datetime
import json
import requests

# pylint: disable=R0903
class User():
    '''defines a wikipedia user by name and id number'''
    def __init__(self, name: str, id_num: int) -> None:
        self.name: str = name
        self.id_num: int = id_num

# pylint: disable=R0902
class Revision():
    '''revision object holds json revision info'''
    def __init__(self, title=None, user=None) -> None:
        # possible params
        self.json: dict = None
        self.revision_id: int = None
        self.title: str = None
        self.timestamp: datetime = None
        self.page_id: int = None
        self.user: User = None
        self.minor: bool = None
        self.tags: list[str] = None
        self.comment: str = None
        self.parent_id: int = None
        self.size: int = None

    def get_contents(self, title='None', username='None'): #start and end time stamps???
        ''' Returns the content of the page at this revision'''

        session = requests.Session()

        url = "https://www.wikipedia.org/w/api.php"

        #check that object contains the correct parameters

        params = {
            "action": "parse",
            "format": "json",
            "oldid": "1136319438", #self.revision_id,
            "prop": "text|links|templates|images|externallinks|sections|revid|displaytitle|iwlinks",
            "formatversion": "2"
        }

        request = session.get(url=url, params=params)
        data = request.json()
        print(data)

    def check_to_id(self, to_id):
        if to_id is None:
            return self.revision_id, self.parent_id
        else:
            return self.revision_id, to_id

    def get_diff(self, to_id: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """

        session = requests.Session()

        url = "https://en.wikipedia.org/w/api.php"

        fromrev, torev = check_to_id(to_id)

        params = {
            #params for Compare API
            #https://www.mediawiki.org/wiki/API:Compare
            'action':"compare",
            'format':"json",
            'fromtitle': self.title,
            'totitle': self.title,
            'fromrev': fromrev,
            'torev': torev
        }

        request = session.get(url=url, params=params)
        data = request.json()

        print(data)
        
