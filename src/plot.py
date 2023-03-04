"""Base class for Plot object"""
from history import History
from revision import Revision

class Plot:
    """Plot base class contains basic plot information"""
    def __init__(self, history):
        self.history: History = history
        self.style: str = "seaborn-darkgrid" #default?
        # _mpl-gallery = histogram
        # _mpl-gallery-nogrid = pie chart
        self.x: list[Revision] = None
        self.title: str = None

    def set_x(self, data): #input parameter could be self.history.anything
        """set x graphing data to any parameter"""
        self.x = data
