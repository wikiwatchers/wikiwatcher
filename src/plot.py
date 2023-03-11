"""Base class for Plot object"""
try:
    from src.exceptions import NoRevisionsException
    from src.history import History
    from src.revision import Revision
except ModuleNotFoundError:
    from exceptions import NoRevisionsException
    from history import History
    from revision import Revision

class Plot:
    """Plot base class contains basic plot information"""
    def __init__(self, history):
        if len(history.revisions) == 0:
            raise NoRevisionsException("No revisions matching filter parameters")
        self.history: History = history
        #self.style: str = "seaborn-darkgrid" #default?
        # _mpl-gallery = histogram
        # _mpl-gallery-nogrid = pie chart
        self.x_axis = []
        self.title: str = None

    def set_x_axis(self, revisions_list: list[Revision],
                   revision_property: str):
        """set x graphing data to any parameter in revision object"""
        for each_rev in revisions_list:
            self.x_axis.append(vars(each_rev)[revision_property])
