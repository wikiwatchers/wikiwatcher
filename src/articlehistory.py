"""defines the collection class for article history"""
import requests
try:
    #pylint:disable=R0801
    from src.revision import Revision, URL
    from src.history import History
    from src.exceptions import BadRequestException
except ModuleNotFoundError:
    from revision import Revision, URL
    from history import History
    from exceptions import BadRequestException

class ArticleHistory(History):
    """article revision collection class"""

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
        self.fill_revisions()

    def init_to_none(self):
        """sets up class data members and initalizes to none"""
        self.pageid: int = None

    def call_wikipedia_api(self):
        """pulls down an article's revision history from the API"""
        session = requests.Session()

        params = {
            "prop": "revisions",
            "titles": self.titles,
            "rvprop": "comment|ids|flags|size|tags|timestamp|user|userid",
            "rvuser": self.user,
            "rvstart": self.rvstart, # pylint: disable=access-member-before-definition
            "rvend": self.rvend,
            "rvdir": "newer",
            "rvlimit": "500"
        } | self.base_params
        if self.titles is None:
            raise BadRequestException("Title Missing")

        rev = session.get(url=URL, params=params)
        data = rev.json()

        try:
            pages = data["query"]["pages"]
            self.json = pages[0]
            self.pageid = self.json["pageid"]
            for each_revision in self.json["revisions"]:
                each_revision["pageid"] = self.pageid
                each_revision["title"] = self.titles
                self.revisions.append(Revision(each_revision))
            if not data.get("continue") is None:
                wp_continue_timestamp_and_id = data["continue"]["rvcontinue"]
                separator_index = wp_continue_timestamp_and_id.index("|")
                self.rvstart = wp_continue_timestamp_and_id[:separator_index]
                self.call_wikipedia_api()
        except KeyError:
            print("Error accessing API with given parameters")

    def get_secondary_category(self):
        """ returns a list of users who have made revisions to the article -
        should only be called after self.revisions has been filled
        """
        return [rev.user for rev in self.revisions]

if __name__ == "__main__":
    art = ArticleHistory(titles="fdjaklfgd;jsa")
    print(art)
