""" Defines exceptions for application-wide error handling """

class BadRequestException(BaseException):
    """ to be raised throughout codebase
    upon discovery of bad user inputs
    """
