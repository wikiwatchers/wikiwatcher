"""defines user history class"""
import requests
try:
    from src.revision import Revision, URL
    from src.history import History
    from src.exceptions import BadRequestException
except ModuleNotFoundError:
    from revision import Revision, URL
    from history import History
    from exceptions import BadRequestException
import mwparserfromhell as mwp

class UserHistory(History):
    """ UserHistory object parses json user contributions """
    def __init__(self, user, startyear=None, startmonth=None, startday=None,
                starthour=None, startminute=None, startsecond=None,
                endyear=None, endmonth=None, endday=None, endhour=None,
                endminute=None, endsecond=None, tags=None, titles=None, keyword=None):
        super().init_to_none()
        self.init_to_none()
        super().__init__(titles, user, keyword, tags, startyear, startmonth, startday,
                         starthour, startminute, startsecond, endyear, endmonth, endday,
                         endhour, endminute, endsecond)
        self.fill_revisions()

    def init_to_none(self):
        """ Sets up class data members and initializes them to None """
        self.user: str = None

    def call_wikipedia_api(self):
        """ Pulls down user's edit history from Wikipedia API """
        session = requests.Session()

        params = {
            "list": "usercontribs",
            "ucprop": "comment|ids|title|flags|size|tags|timestamp|user|userid",
            "ucuser": self.user,
            "ucstart": self.rvstart, # pylint: disable=access-member-before-definition
            "ucend" : self.rvend,
            "ucdir": "newer",
            "uclimit": "500"
        } | self.base_params
        if self.user is None:
            raise BadRequestException("User name missing")

        request = session.get(url=URL, params=params)
        data = request.json()

        try:
            self.json = data["query"]["usercontribs"]
            for each_revision in self.json:
                self.revisions.append(Revision(each_revision))
            if not data.get("continue") is None:
                wp_continue_timestamp_and_id = data["continue"]["uccontinue"]
                separator_index = wp_continue_timestamp_and_id.index("|")
                self.rvstart = wp_continue_timestamp_and_id[:separator_index]
                self.call_wikipedia_api()
        except BadRequestException:
            print("Data not found")

    def get_secondary_category(self):
        """ returns a list of articles which have been edited by the user -
        should only be called after self.revisions has been filled
        """
        return [rev.title for rev in self.revisions]