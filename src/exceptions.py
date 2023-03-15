""" Defines exceptions for application-wide error handling """

class BadRequestException(Exception):
    """ to be raised throughout codebase
    upon discovery of bad user inputs
    """

class NoRevisionsException(Exception):
    """ to be raised throughout codebase
    upon discovery of no revisions fitting request's filters
    """
