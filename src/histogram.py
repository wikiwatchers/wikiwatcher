import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from plot import Plot
from datetime import datetime
import time
try:
    from src.articlehistory import ArticleHistory
except ModuleNotFoundError:
        from articlehistory import ArticleHistory

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)
        self.num_bins = None
        self.y_axis_label = "Number of edits"
        self.x_axis_label = "Date"

        self.x_axis = self.pull_dates_from_history()
        self.plot_graph()
        #print(self.x_axis)

    def pull_dates_from_history(self):
        datetime_list = []
        for each_rev in self.history.revisions:
            this_datetime = each_rev.timestamp_to_datetime()
            datetime_list.append(mdates.date2num(this_datetime))
        return np.array(datetime_list)
    
    def set_num_bins(self):
        #3 month or under range, 1 bin per day
        bin_width = 1
        minimmum = np.min(self.x_axis)
        maximmum = np.max(self.x_axis)
        bound_min = -1.0 * (minimmum % bin_width - minimmum)
        bound_max = maximmum - maximmum % bin_width + bin_width
        n = int((bound_max - bound_min) / bin_width) + 1
        self.num_bins = np.linspace(bound_min, bound_max, n)
        
    
    def plot_graph(self):

        fig, ax = plt.subplots()

        locator = mdates.AutoDateLocator()
        self.set_num_bins()

        ax.hist(self.x_axis, bins=self.num_bins, color="lightblue", edgecolor="black", range=(self.x_axis[0], self.x_axis[len(self.x_axis)-1]))


        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

        plt.xticks(rotation=45)

        plt.ylabel(self.y_axis_label)
        plt.xlabel(self.x_axis_label)

        fig.tight_layout()

        plt.show()

if __name__=="__main__":
    article = ArticleHistory("Cat", startyear=2004, endyear=2004, endmonth=10, startmonth=6)
    Histogram(article)
