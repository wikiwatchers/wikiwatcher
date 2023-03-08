import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from plot import Plot
from articlehistory import ArticleHistory
from datetime import datetime
import time

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)

        self.x_axis = self.pull_dates_from_history()
        self.plot_graph()

        #print(self.x_axis)

    def pull_dates_from_history(self):
        datetime_list = []
        for each_rev in self.history.revisions:
            this_datetime = each_rev.timestamp_to_datetime()
            datetime_list.append(mdates.date2num(this_datetime))
        return np.array(datetime_list)
    
    def plot_graph(self):

        fig, ax = plt.subplots()

        ax.hist(self.x_axis, bins=50, color="lightblue", edgecolor="black")

        locator = mdates.AutoDateLocator()
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
        plt.xticks(rotation=45)

        plt.show()
        


if __name__=="__main__":
    article = ArticleHistory("Techno", startyear=2001, endyear=2004)
    Histogram(article)
