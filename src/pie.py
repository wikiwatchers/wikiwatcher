""" Pie chart for visualizing which articles a user has edited
or which users have edited an article
"""
import matplotlib.pyplot as plt
from random import random
from datetime import datetime
import numpy as np
try:
    from src.exceptions import NoRevisionsException, BadRequestException
    from src.plot import Plot
    from src.history import History
except ModuleNotFoundError:
    from exceptions import NoRevisionsException
    from plot import Plot
    from history import History

class Pie(Plot):
    """ the pie chart itself, graph attribute contains a pyplot.Figure """
    def __init__(self, history):
        super().__init__(history)

        self.x_axis = history.get_secondary_category()
        self.graph = self.plot_graph()

    def plot_graph(self):
        """ sets up the figure and returns it """
        labels = tuple(set(self.x_axis))
        sizes = [self.x_axis.count(category) for category in labels]
        fig_size_inches = (6,6)
        num_labels = len(labels)
        match num_labels:
            case 0:
                raise NoRevisionsException("No revisions matching filter parameters")
            case _ if 1 < num_labels < 10:
                fig_size_inches = (6,6)
                pct_distance = 1.4
                label_distance = 1.8
            case _ if 11 < num_labels < 30:
                fig_size_inches = (10,10)
                pct_distance = 1.3
                label_distance = 1.6
            case _ if 30 < num_labels < 100:
                fig_size_inches = (14,14)
                pct_distance = 1.2
                label_distance = 1.4
            case _:
                fig_size_inches = (18,18)
                pct_distance = 1.1
                label_distance = 1.2

        fig, axes = plt.subplots(layout="constrained", figsize=fig_size_inches)
        plt.rcParams["figure.constrained_layout.use"] = True

        _, labels, percents = axes.pie(sizes, labels=labels, autopct=make_autopct(sizes),
               pctdistance=pct_distance, labeldistance=label_distance, rotatelabels=True)
        for label, percent in zip(labels, percents):
            percent.set_rotation(label.get_rotation())

        if not self.history.titles is None and not self.history.user is None:
            raise BadRequestException(
                "Specifying both user and article title - pie chart redundant"
                )
        if not self.history.titles is None:
            title = f"Users who have made revisions to {self.history.titles}\n"
        else:
            title = f"Articles revised by {self.history.user}\n"
        if not self.history.rvstart is None:
            title += f"from {datetime.fromisoformat(self.history.rvstart)}\n"
        if not self.history.rvend is None:
            title += f"to {datetime.fromisoformat(self.history.rvend)}\n"
        fig.suptitle(title)
        return fig

def make_autopct(values):
    """ see
    https://stackoverflow.com/questions/6170246/
    how-do-i-use-matplotlib-autopct
    enables pie chart to display both percent and raw count for each wedge
    """
    def make_percent_and_count_string(count):
        total = sum(values)
        val = int(round(count*total/100.0))
        return f"{count:.2f}% ({val:d})"
    return make_percent_and_count_string
