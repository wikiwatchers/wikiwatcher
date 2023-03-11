"""contains history base class attributes and timestamp modification"""

import json
from datetime import datetime
from abc import abstractmethod
try:
    from src.revision import Revision
    from src.exceptions import BadRequestException
except ModuleNotFoundError:
    from revision import Revision
    from exceptions import BadRequestException

class History:
    """history base class initalization"""

    def __init__(self, titles=None, user=None, keyword=None, tags=None,
                 start_year=None, start_month=None, start_day=None, start_hour=None,
                 start_minute=None, start_second=None, end_year=None, end_month=None,
                 end_day=None, end_hour=None, end_minute=None, end_second=None):
        self.init_to_none()
        self.titles = titles
        self.user = user
        self.keyword = keyword
        self.tags = tags
        start_timestamp_is_specified = start_year or start_month or start_day \
                                    or start_hour or start_minute or start_second
        end_timestamp_is_specified = end_year or end_month or end_day \
                                  or end_hour or end_minute or end_second
        if start_timestamp_is_specified:
            self.rvstart = format_timestamp(start_year, start_month, start_day,
                                            start_hour, start_minute, start_second)
        if end_timestamp_is_specified:
            self.rvend =  format_timestamp(end_year, end_month, end_day,
                                            end_hour, end_minute, end_second)
        self.base_params = {
           "action": "query",
            "format": "json",
            "formatversion": "2",
        }

    def init_to_none(self):
        """sets up class data members and initalizes to none"""
        self.json: dict = None
        self.titles: str = None
        self.user: str = None
        self.keyword: str = None
        self.tags: list[str] = None
        self.rvstart: str = None
        self.rvend: str = None
        self.revisions: list[Revision] = None

    def revisions_as_json(self) -> str:
        """ returns internal revisions list as a JSON string
         where revisions are separated by newlines for readability """
        if self.revisions is None:
            return None  # raise error?
        ret = [rev.json for rev in self.revisions]
        ret_json = json.dumps(ret)
        # adding break tags makes this invalid json!
        # just for display/testing
        ret_json = ret_json.replace("},", "},<br/>")
        return ret_json

    def filter(self):
        """calls filter helper functions"""
        if self.tags is not None:
            self.filter_by_tags()
        if self.keyword is not None:
            self.filter_by_keyword()

        if len(self.revisions) == 0:
            print("No revisions found matching your search parameters")

    def filter_by_keyword(self):
        """filters list of revisions by keyword"""
        for rev in self.revisions.copy():
            if rev.contains_keyword(self.keyword) is False:
                self.revisions.remove(rev)

    def filter_by_tags(self):
        """filters list of revisions by tags"""
        for rev in self.revisions.copy():
            if rev.contains_tag(self.tags) is False:
                self.revisions.remove(rev)

    @abstractmethod
    def call_wikipedia_api(self):
        """ history subclasses must implement a call to the external API """

    def fill_revisions(self):
        """ uses derived class call_wikipedia_api and filter methods
        to retrieve revisions from wikipedia
        """
        self.revisions = []
        self.call_wikipedia_api()
        self.filter()

    @abstractmethod
    def get_secondary_category(self):
        """ Returns a list of the secondary category for the subtype of revision
        that implements the function; e.x. for ArticleHistory, this should return a
        list of users; for UserHistory, a list of articles
        """

def validate_datetime_params(bad_datetime: Exception, year, month, day, hour, minute, second):
    """ ensures all datetime params fall into valid ranges (ex hours 0 through 23) """
    # could this entirely replace the order-validation in format_timestamp?
    try:
        datetime(year=year, month=month or 1, day=day or 1,
                 hour=hour or 0, minute=minute or 0, second=second or 0)
    except ValueError as val_err:
        raise bad_datetime from val_err

def format_timestamp(year=None, month=None, day=None,
                     hour=None, minute=None, second=None):
    """ cats our user's requested date/time values into a wikipedia-friendly string
    and validates that user gave us a correct date/time
    """
    bad_datetime = BadRequestException("invalid date/time specification")
    no_more_params = False
    if not year is None:
        ret = str(year)
    else:
        raise bad_datetime
    validate_datetime_params(bad_datetime, year, month,
                             day, hour, minute, second)
    index = 0
    for param in [month, day, hour, minute, second]:
        if no_more_params and not param is None:
            raise bad_datetime
        if not param is None:
            ret += str(param).rjust(2, "0")
        else:
            no_more_params = True
            if index in [2, 3, 4]:  # hour minute and second should default to 0
                ret += "00"
            else:  # all other params default to 1
                ret += "01"
        index += 1
    return ret
