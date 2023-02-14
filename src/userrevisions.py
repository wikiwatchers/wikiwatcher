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
        self.revisions = []
        print("init json:")
        for i in initjson:
            print("this:")
            #print(i)
            revisionjson = i
            revisionjson['pageid'] = i['pageid']
            revisionjson['title'] = i['title']
            print("revisionjson:")
            print(revisionjson)
            this_revision = Revision(revisionjson)
            print(this_revision.pageid)
            self.revisions.append(this_revision)

    def init_to_none(self):
        '''sets up class data members and initializes them to None '''
        self.revisions: list[Revision] = None
        self.userid: int = None
        self.username: str = None

    
