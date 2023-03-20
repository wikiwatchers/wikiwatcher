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
    """ representst the pie chart associated with the history object passed in
    returns a pyplot.Figure from its get_graph() method
    """
    def __init__(self, history):
        super().__init__(history)

        self.x_axis = self.get_x_axis_data("user")
        self.labels = tuple(set(self.x_axis))
        self.sizes = [self.x_axis.count(category) for category in self.labels]

    def get_x_axis_data(self, revision_property: str):
        return super().get_x_axis_data(revision_property)

    def get_graph(self) -> plt.Figure:
        """ sets up the pychart.Figure object and returns it """
        if not self.history.titles is None and not self.history.user is None:
            raise BadRequestException(
                "Specifying both user and article title - pie chart redundant")
        fig_size_inches, pct_distance, label_distance = self.size_of_png()
        fig, axes = plt.subplots(layout="constrained", figsize=fig_size_inches)
        autopct_string = make_autopct(self.sizes)

        _, labels, percents = axes.pie(self.sizes, labels=self.labels, autopct=autopct_string,
               pctdistance=pct_distance, labeldistance=label_distance, rotatelabels=True)
        for label, percent in zip(labels, percents):
            percent.set_rotation(label.get_rotation())
        title = self.generate_pie_title()
        fig.suptitle(title)
        plt.rcParams["figure.constrained_layout.use"] = True
        return fig

    def size_of_png(self):
        """ uses number of wedges to determine necessary image size and chart parameters
        returns a 3-tuple of (
            tuple of (width_inches: int, height_inches: int),
            distance_to_percent: float,
            distance_to_label: float
        ) Need to improve this to use some mathematical algorithm instead of cases
        """
        fig_size_inches = (-1,-1)
        pct_distance = -1.0
        label_distance = -1.0
        num_labels = len(self.labels)
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
        return (fig_size_inches, pct_distance, label_distance)

    def generate_pie_title(self) -> str:
        """ Generates a title for the graph depending on what was requested """
        title = ""
        if not self.history.titles is None:
            title = f"Users who have made revisions to {self.history.titles}\n"
        else:
            title = f"Articles revised by {self.history.user}\n"
        if not self.history.rvstart is None:
            title += f"from {datetime.fromisoformat(self.history.init_rvstart_for_charts)}\n"
        if not self.history.rvend is None:
            title += f"to {datetime.fromisoformat(self.history.rvend)}\n"
        return title

def make_autopct(values) -> str:
    """ see
    https://stackoverflow.com/questions/6170246/
    how-do-i-use-matplotlib-autopct
    takes in a list of values
    returns a function which processes each element of the list,
    returning a string containing formatted percent and count values
    for each value
    """
    def make_percent_and_count_string(value):
        total = sum(values)
        val = int(round(value*total/100.0))
        return f"{value:.2f}% ({val:d})"
    return make_percent_and_count_string
