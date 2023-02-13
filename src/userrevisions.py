'''defines user revisions class'''
import requests
from revision import Revision
import mwparserfromhell as mwp


URL = "https://www.wikipedia.org/w/api.php"

class UserRevisions():
    '''userrevision object parses json user contributions into consistent '''

    def __init__(self, initjson: dict) -> None:
        self.json: dict = initjson
        self.init_to_none()

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.revisions: list[Revision] = None
        self.userid: int = None
        self.username: str = None

    def get_content(self):  # start and end time stamps???
        ''' Returns list of user's contributions '''

        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            #"ucuser": "Jimbo%20Wales"
            "ucuser": self.username
        }
        if self.username is None:
            raise AttributeError("User name missing")
        request = session.get(url=URL, params=params)
        data = request.json()['parse']['text']['*']
        return str(mwp.parse(data))
