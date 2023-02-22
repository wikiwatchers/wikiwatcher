'''defines the collection class for article history'''
import requests
from datetime import datetime
from src.revision import Revision
from src.history import format_timestamp,History

#pylint: disable=C0303,R0913,R0914
class ArticleHistory(History):
    '''article revision collection class'''
    def __init__(self, titles, user=None, keyword=None, tags=None,
                startyear=None, startmonth=None, startday=None, 
                starthour=None, startminute=None, startsecond=None, 
                endyear=None, endmonth=None, endday=None, endhour=None, 
                endminute=None, endsecond=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(titles, user, keyword, tags,
                        startyear, startmonth, startday, 
                        starthour, startminute, startsecond,
                        endyear, endmonth, endday, 
                        endhour, endminute, endsecond)

        self.call_api()
        #filter()

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.pageid: int = None
    #pylint:disable=W0105
    '''
    def filter(self, user, keyword, tags, arvstart, arvend=None):
        #filters article revisions using various arguments
        pass
    '''
    
    def call_api(self):
        '''pulls down an article's revision history from the API'''
        self.revisions = []
        session = requests.Session()

        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "continue": "||",
            "titles": self.titles,
            "rvprop": "comment|ids|flags|size|timestamp|user|userid",
            "rvslots": "*",
            "formatversion": "2",
            "rvuser": self.user,
            "rvstart": self.rvstart,
            "rvend": self.rvend
        }

        rev = session.get(url=url, params=params)
        data = rev.json()

        try:
            pages = data["query"]["pages"]
            self.json = pages[0]
            self.pageid = self.json["pageid"]

            for each_revision in self.json["revisions"]:
                self.revisions.append(Revision(each_revision))
            
        except KeyError:
            print("Data not found")
