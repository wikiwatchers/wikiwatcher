import matplotlib.pyplot as plt
from random import random
import numpy as np
try:
    from src.exceptions import NoRevisionsException, BadRequestException
    from src.plot import Plot
    from src.history import History
    from src.revision import timestamp_to_datetime
except ModuleNotFoundError:
    from exceptions import NoRevisionsException
    from plot import Plot
    from history import History
    from revision import timestamp_to_datetime

class Pie(Plot):
    def __init__(self, history):
        super().__init__(history)
        
        self.x_axis = history.get_secondary_category()
        self.graph = self.plot_graph()

    def plot_graph(self):

        labels = tuple(set(self.x_axis))
        sizes = [self.x_axis.count(category) for category in labels]
        fig_size_inches = (6,6)
        num_labels = len(labels)
        match num_labels:
            case 0:
                raise NoRevisionsException("No revisions matching filter parameters")
            case _ if 1 < num_labels < 10:
                fig_size_inches = (6,6)
            case _ if 11 < num_labels < 30:
                fig_size_inches = (10,10)
            case _ if 30 < num_labels < 100:
                fig_size_inches = (14,14)
            case default:
                fig_size_inches = (18,18)

        fig, ax = plt.subplots(layout="constrained", figsize=fig_size_inches)
        plt.rcParams["figure.constrained_layout.use"] = True

        _, labels, percents = ax.pie(sizes, labels=labels, autopct="%1.1f%%",
               pctdistance=1.2, labeldistance=1.4, rotatelabels=True)
        for label, percent in zip(labels, percents):
            percent.set_rotation(label.get_rotation())

        if not self.history.titles is None and not self.history.user is None:
            raise BadRequestException("Specifying both user and article title - pie chart redundant")
        elif not self.history.titles is None:
            title = f"Users who have made revisions to {self.history.titles}\n"
        else:
            title = f"Articles revised by {self.history.user}\n"
        if not self.history.rvstart is None:
            title += f"from {timestamp_to_datetime(self.history.rvstart)}\n"
        if not self.history.rvend is None:
            title += f"to {self.history.rvend}\n"
        fig.suptitle(title)
        return fig

    def get_proportion_of_category(self, category_list, category):
        return category_list.count(category)