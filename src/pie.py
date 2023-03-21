""" Pie chart for visualizing which articles a user has edited
or which users have edited an article
"""
from math import ceil
import matplotlib.pyplot as plt
from random import random
from datetime import datetime
import numpy as np
try:
    from src.exceptions import BadRequestException
    from src.plot import Plot
    from src.history import History
    from src.userhistory import UserHistory
    from src.articlehistory import ArticleHistory
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

        if type(self.history) == UserHistory:
            self.x_axis = self.get_x_axis_data("title")
        elif type(self.history) == ArticleHistory:
            self.x_axis = self.get_x_axis_data("user")
        self.labels = tuple(set(self.x_axis))
        self.sizes = [self.x_axis.count(category) for category in self.labels]

    def get_graph(self) -> plt.Figure:
        """ sets up the pychart.Figure object and returns it """
        if not self.history.titles is None and not self.history.user is None:
            raise BadRequestException(
                "Specifying both user and article title - pie chart redundant")
        fig_size_inches, pct_distance, label_distance, fontsize = self.size_of_png()
        fig, axes = plt.subplots(layout="constrained", figsize=fig_size_inches)
        autopct_string = make_autopct(self.sizes)

        _, labels, percents = axes.pie(self.sizes, labels=self.labels, autopct=autopct_string,
               pctdistance=pct_distance, labeldistance=label_distance, rotatelabels=True,
               textprops={"fontsize": fontsize})
        for label, percent in zip(labels, percents):
            percent.set_rotation(label.get_rotation())
            if len(label.get_text()) > 20:
                label.set_text(label.get_text()[0:21] + "...")
        title = self.generate_pie_title()
        fig.suptitle(title)
        #plt.rcParams["figure.constrained_layout.use"] = True
        return fig

    def size_of_png(self):
        """ uses number of wedges to determine necessary image size and chart parameters
        returns a 3-tuple of (
            tuple of (width_inches: int, height_inches: int),
            distance_to_percent: float,
            distance_to_label: float,
            fontsize: int
        ) Need to improve this to use some mathematical algorithm instead of cases
        """
        fig_size_inches = (-1,-1)
        pct_distance = -1.0
        label_distance = -1.0
        fontsize = 12
        num_labels = len(self.labels)
        match num_labels:
            case _ if 1 < num_labels < 10:
                fig_size_inches = (8,8)
                pct_distance = 1.4
                label_distance = 1.8
            case _ if 10 < num_labels < 20:
                fig_size_inches = (10,10)
                pct_distance = 1.4
                label_distance = 1.8
            case _ if 20 < num_labels < 30:
                fig_size_inches = (12,12)
                pct_distance = 1.3
                label_distance = 1.6
            case _ if 30 < num_labels < 100:
                fig_size_inches = (16,16)
                pct_distance = 1.2
                label_distance = 1.4
                fontsize -= 2
            case _:
                fig_size_inches = (20,20)
                pct_distance = 1.1
                label_distance = 1.2
                fontsize -= 4
        return (fig_size_inches, pct_distance, label_distance, fontsize)

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
