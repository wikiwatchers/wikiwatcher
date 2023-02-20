""" REMOVE ON MERGE defines a base class for user and article histories"""
from src.exceptions import BadRequestException

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
