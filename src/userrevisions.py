'''defines user revisions class'''
import requests
from revision import Revision, User

class UserRevisions():
    '''User revision object holds a list of user's revisions'''
    def __init__(self) -> None:
        # possible params
        self.json: dict = None
        self.user: User = None
        self.revisions: list[Revision] = None

    def get_contents(self):
        '''notes'''

        session = requests.Session()

        url = "https://www.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "format": "json",
            "list": "usercontribs",
            "formatversion": "2",
            #ucuser - placeholder
             "ucuser": "Jimbo%20Wales" 
        }
        try:
            request = session.get(url=url, params=params)
        except Exception as exc:
            raise SystemExit("User Name missing") from exc
        data = request["query"].json()
        print(data)
