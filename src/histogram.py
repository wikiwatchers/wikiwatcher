""" temporary to calm pylint down - should be filled in by author """
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
from dateutil import parser
try:
    from src.articlehistory import ArticleHistory
    from src.plot import Plot
except ModuleNotFoundError:
    from articlehistory import ArticleHistory
    from plot import Plot

class Histogram(Plot):
    """ temporary to calm pylint down - should be filled in by author """
    def __init__(self, history):
        super().__init__(history)
        self.num_bins = None
        self.y_axis_label = "Number of edits"
        self.x_axis_label = "Date"
        self.title = "Number of Edits per Date"
        self.x_axis = self.get_x_axis_data()

    def get_x_axis_data(self, revision_property: str = "timestamp"):
        """pulls the datetime from each history object
        turns the datetime into a format useable by matplotlib
        then puts it into a numpy array"""
        timestamp_list = super().get_x_axis_data(revision_property)
        new_datetime = []
        for each_timestamp in timestamp_list:
            new_datetime.append(mdates.date2num(parser.isoparse(each_timestamp)))
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

    def get_graph(self):
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
