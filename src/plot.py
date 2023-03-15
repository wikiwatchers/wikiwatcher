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
        self.graph = None
        self.x_axis = []
        self.x_axis_label: str = None
        self.y_axis_label: str = None
        self.title: str = None

    def get_x_axis_data(self,
                   revision_property: str):
        """set x graphing data to any parameter in revision object"""
        return self.history.get_list_of_revision_key_data(revision_property)
