import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
try:
    from src.articlehistory import ArticleHistory
    from src.plot import Plot
except ModuleNotFoundError:
    from articlehistory import ArticleHistory
    from plot import Plot

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)

        self.x_axis = self.pull_dates_from_history()
        self.graph = self.plot_graph()

    def pull_dates_from_history(self):
        datetime_list = []
        for each_rev in self.history.revisions:
            this_datetime = each_rev.timestamp_to_datetime()
            datetime_list.append(mdates.date2num(this_datetime))
        return np.array(datetime_list)
    
    def plot_graph(self):

        fig, ax = plt.subplots()

        ax.hist(self.x_axis, bins=50, color="lightblue", edgecolor="black", range=(self.x_axis[0], self.x_axis[len(self.x_axis)-1]))

        locator = mdates.AutoDateLocator()
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

        plt.xticks(rotation=45)
        plt.tight_layout()

        return fig

if __name__=="__main__":
    article = ArticleHistory("Cat", startyear=2004, endyear=2008)
    Histogram(article)
