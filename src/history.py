'''contains history base class attributes and timestamp modification'''

from revision import Revision
from src.exceptions import BadRequestException

class History:
    '''history base class initalization'''
    def __init__(self, titles=None, user=None, keyword=None, tags=None, 
        start_year=None, start_month=None, start_day=None, start_hour=None, 
        start_minute=None, start_second=None, end_year=None, end_month=None, 
        end_day=None, end_hour=None, end_minute=None, end_second=None):
        self.init_to_none()
        self.titles = titles
        self.user = user
        self.keyword = keyword
        self.tags = tags
        self.rvstart = format_timestamp(start_year, start_month, start_day, 
                                        start_hour, start_minute, start_second)
        self.rvend =  format_timestamp(end_year, end_month, end_day, 
                                        end_hour, end_minute, end_second)

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.json: dict = None
        self.titles: str = None
        self.user: str = None
        self.keyword: str = None
        self.tags: list[str] = None
        self.rvstart: str = None 
        self.rvend: str = None
        self.revisions: list[Revision] = None

def format_timestamp(year, month, day, hour, minute, second):
    """ cats our user's requested date/time values into a wikipedia-friendly string
    and validates that user gave us a correct date/time """
    if year:
        ret = str(year)
    else:
        raise BadRequestException("invalid date/time specification")
    ret += str(month).rjust(2, "0") if month else "01"
    ret += str(day).rjust(2, "0") if day else "01"
    ret += str(hour).rjust(2, "0") if hour else "00"
    ret += str(minute).rjust(2, "0") if minute else "00"
    ret += str(second).rjust(2, "0") if second else "01"
    return ret
