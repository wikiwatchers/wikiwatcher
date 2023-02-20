'''defines user history class'''
import datetime
import requests
from history import History
from exceptions import BadRequestException
import mwparserfromhell as mwp

URL = "https://www.wikipedia.org/w/api.php"

class UserHistory():
    '''userhistory object parses json user contributions '''

    def __init__(self, username, keyword=None, article=None):
        self.init_to_none()
        self.username = username
        self.keyword = keyword
        self.article = article
        self.get_history()
        #filter here

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.username: str = None

    def get_history(self):
        ''' Gets user history '''
        self.revisions = []
        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": self.username
        }
        if self.username is None:
            raise BadRequestException("User name missing")

        request = session.get(url=URL, params=params)

        data = request.json()['query']['usercontribs']

        try:
            self.json = data
            for revision in self.json:
                self.revisions.append(revision)
        except BadRequestException:
            print("No revisions")

        print(self.revisions[0])
        return str(mwp.parse(data))
        