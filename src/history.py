"""contains history base class attributes and timestamp modification"""

import json
from datetime import datetime
from abc import abstractmethod
try:
    from src.revision import Revision
    from src.exceptions import BadRequestException, NoRevisionsException
except ModuleNotFoundError:
    from revision import Revision
    from exceptions import BadRequestException, NoRevisionsException

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
        try:
            if start_timestamp_is_specified:
                self.rvstart = datetime(year=start_year, month=start_month or 1,
                                        day=start_day or 1, hour=start_hour or 0,
                                        minute=start_minute or 0, second = start_second or 0
                                        ).isoformat()
                self.init_rvstart_for_charts = self.rvstart
            if end_timestamp_is_specified:
                self.rvend = datetime(year=end_year, month=end_month or 1,
                                        day=end_day or 1, hour=end_hour or 0,
                                        minute=end_minute or 0, second = end_second or 0
                                        ).isoformat()
        except (ValueError, TypeError) as val_err:
            raise BadRequestException("invalid date/time specification") from val_err

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
        self.init_rvstart_for_charts: str = None
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
        if len(self.revisions) == 0:
            raise NoRevisionsException("No revisions matching filter parameters")

    def get_list_of_revision_key_data(self, revision_key):
        """returns a list of attributes pulled from revisions list
        argument is the attribute to pull from each revision"""
        revision_key_list = []
        try:
            for each_rev in self.revisions:
                revision_key_list.append(each_rev.get_revision_key(revision_key))
        except KeyError:
            print("Revisions do not contain this key")
        return revision_key_list
