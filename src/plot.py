"""Base class for Plot object"""
try:
    from src.history import History
    from src.revision import Revision
except ModuleNotFoundError:
    from history import History
    from revision import Revision


class Plot:
    """Plot base class contains basic plot information"""
    def __init__(self, history):
        self.history: History = history
        #self.style: str = "seaborn-darkgrid" #default?
        # _mpl-gallery = histogram
        # _mpl-gallery-nogrid = pie chart
        self.x_axis = []
        self.x_axis_label: str = None
        self.y_axis_label: str = None
        self.title: str = None

    def set_x_axis(self, revisions_list: list[Revision],
                   revision_property: str):
        """set x graphing data to any parameter in revision object"""
        for each_rev in revisions_list:
            self.x_axis.append(vars(each_rev)[revision_property])
