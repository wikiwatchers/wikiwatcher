class history:
    def __init__(self, titles=None, user=None, keyword=None, tags=None, 
        start_year=None, start_month=None, start_day=None, start_hour=None, start_minute=None, start_second=None,
        end_year=None, end_month=None, end_day=None, end_hour=None, end_minute=None, end_second=None):
        self.init_to_none()
        self.titles = titles
        self.user = user
        self.keyword = keyword
        self.tags = tags
        self.format_timestamp(start_year, start_month, start_day, start_hour, start_minute, 
        start_second, end_year, end_month, end_day, end_hour, end_minute, end_second)

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.json: dict = None
        self.titles: string = None
        self.user: str = None
        self.keyword: str = None
        self.tags: list[str] = None
        self.arvstart: str = None 
        self.arvend: str = None
        self.revisions: list[Revision] = None

    def format_timestamp(self):
        pass