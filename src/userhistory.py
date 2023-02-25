'''defines user history class'''
import datetime
import requests
from src.history import History
from src.exceptions import BadRequestException
import mwparserfromhell as mwp

URL = "https://www.wikipedia.org/w/api.php"

class UserHistory(History):
    '''userhistory object parses json user contributions '''
    def __init__(self, username, keyword=None, article=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(username, keyword, article)

        self.username = username
        self.keyword = keyword
        self.article = article
        self.call_wikipedia_api()
        #filter here

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.username: str = None

    def call_wikipedia_api(self):
        ''' pulls down user's edit history from Wikipedia API '''
        self.revisions = []
        session = requests.Session()

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            "ucuser": self.username
        } | self.base_params
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
