class history:
    def __init__(self, titles=None, user=None, keyword=None, tags=None, 
        start_year=None, start_month=None, start_day=None, start_hour=None, start_minute=None, start_second=None,
        end_year=None, end_month=None, end_day=None, end_hour=None, end_minute=None, end_second=None):
        self.init_to_none()
        self.titles = titles
        self.user = user
        self.keyword = keyword
        self.tags = tags
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.start_second = start_second
        self.end_year = end_year
        self.end_month = end_month
        self.end_minute = end_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.end_second = end_second

        format_timestamp()

    def init_to_none(self):
        '''sets up class data members and initalizes to none'''
        self.json: dict = None
        self.titles: string = None
        self.user: str = None
        self.keyword: str = None
        self.tags: list[str] = None
        self.start_year: int = None
        self.start_month: int = None
        self.start_day: int = None
        self.start_hour: int = None
        self.start_minute: int = None
        self.start_second: int = None
        self.end_year: int = None
        self.end_month: int = None
        self.end_minute: int = None
        self.end_hour: int = None
        self.end_minute: int = None
        self.end_second: int = None
        self.revisions: list[Revision] = None

    def format_timestamp(self):
        pass