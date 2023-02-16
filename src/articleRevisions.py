from Revision import Revision, User
from datetime import datetime

class ArticleRevisions(self, titles, rvstart, rvend=None):
    def __init__(self):
        self.titles = titles
        self.rvstart = rvstart
        self.rvend = rvend #if None, pull single revision from rvstart
        self.revisions: list[Revision] = None

    def filter_by_keyword(self, keyword):

    def filter_by_tags(self, tags[]): #list of strings
