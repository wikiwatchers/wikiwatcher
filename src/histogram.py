"""Histogram class, accepts a History object and
makes a plot based on datetime"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from plot import Plot
from datetime import datetime
import time
try:
    from src.articlehistory import ArticleHistory
    from src.revision import timestamp_to_datetime
except ModuleNotFoundError:
    from articlehistory import ArticleHistory
    from revision import timestamp_to_datetime

class Histogram(Plot):
    """Histogram class, accepts a History object and
    plots a histogram using datetime array"""
    def __init__(self, history):
        super().__init__(history)
        self.num_bins = None
        self.y_axis_label = "Number of edits"
        self.x_axis_label = "Date"
        self.title = "Number of Edits per Date"

        self.x_axis = self.get_x_axis_data()
        self.graph = self.plot_graph()

    def get_x_axis_data(self):
        """pulls the datetime from each history object
        turns the datetime into a format useable by matplotlib
        then puts it into a numpy array"""
        timestamp_list = super().get_x_axis_data("timestamp")
        new_datetime = []
        for each_timestamp in timestamp_list:
            new_datetime.append(mdates.date2num(timestamp_to_datetime(each_timestamp)))
        return np.array(new_datetime)

    def set_num_bins(self):
        """sets the number of bins - approximately one bin per day"""
        bin_width = 1
        minimum = np.min(self.x_axis)
        maximum = np.max(self.x_axis)
        bound_min = -1.0 * (minimum % bin_width - minimum)
        bound_max = maximum - maximum % bin_width + bin_width
        num = int((bound_max - bound_min) / bin_width) + 1
        self.num_bins = np.linspace(bound_min, bound_max, num)
        print(self.num_bins)

    def plot_graph(self):
        """graphs the histogram using matplot lib"""
        fig, axe = plt.subplots(layout="constrained")
        self.set_num_bins()
        axe.hist(self.x_axis, bins=self.num_bins, color="lightblue",
                edgecolor="black", range=(self.x_axis[0], self.x_axis[len(self.x_axis)-1]))
        locator = mdates.AutoDateLocator()
        axe.xaxis.set_major_locator(locator)
        axe.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
        plt.xticks(rotation=45)
        plt.ylabel(self.y_axis_label)
        plt.xlabel(self.x_axis_label)
        plt.title(self.title)
        plt.rcParams['figure.constrained_layout.use'] = True
        #plt.show()
        return fig

if __name__=="__main__":
    article = ArticleHistory(titles="Cat", startyear=2021, startmonth=2,
                         endyear=2021, endmonth=3)
    Histogram(article)
