from datetime import datetime


class User():
    def __init__(self, name: str, id: int) -> None:
        self.name: str = name
        self.id: int = id


class Revision():
    def __init__(self) -> None:
        # possible params
        self.json: dict = None
        self.id: int = None
        self.timestamp: datetime = None
        self.pageId: int = None
        self.user: User = None
        self.minor: bool = None
        self.tags: list[str] = None

        # present in Usercontribs but not Pagehistory
        self.parentId: int = None
        # present in Pagehistory but not Usercontribs
        self.size: int = None
        # TODO

    def get_contents(self):
        """ Returns the content of the page at this revision
        Hits mediawiki.org API with
        "action": "query",
        "prop": "revisions",
        "rvprop": "content"
        """
        # TODO
        pass

    def get_diff(self, toId: int = None):
        """ Returns the difference between this revision and its parent 
        in this revision's article's history, unless a toId is specified in
        which case this revision is compared with toId.
        """
        if toId is None:  # compare with parent
            if self.parentId is None:  # articleHistory, handle elsewhere?
                pass  # raise an exception to be caught in articleHistory? TODO
            else:  # userHistory, handle here
                pass  # TODO
        else:  # compare self to toid, hit getrevision endpoint
            pass  # TODO
