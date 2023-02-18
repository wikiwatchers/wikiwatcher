'''defines user history class'''
import datetime
import requests
from history import history
import mwparserfromhell as mwp

URL = "https://www.wikipedia.org/w/api.php"

class UserHistory():
    '''userhistory object parses json user contributions '''

    def __init__(self, initjson: dict) -> None:
        self.json: dict = initjson
        self.init_to_none()

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.history: history = None
        self.userid: int = None
        self.username: str = None

    def get_history(self):
        ''' Gets user history '''

        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": self.username
        }
        if self.username is None:
            raise AttributeError("User name missing")
        request = session.get(url=URL, params=params)
        # if self.keyword is not None:
            # Do filtering with keyword
        data = request.json()['query']['usercontribs']
        return str(mwp.parse(data))

        