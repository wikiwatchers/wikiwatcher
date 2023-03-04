import matplotlib.pyplot as plt
import numpy as np
from plot import Plot
from articlehistory import ArticleHistory
from datetime import datetime
import time

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)
        
        unix_time_list = self.datetime_to_unixtime()
        self.set_x_axis(unix_time_list)

        self.plot_graph()

        print(self.x_axis)
        print(type(self.x_axis))

    def datetime_to_unixtime(self):
        unix_time_list = []
        for each_rev in self.history.revisions:
            unix_time_list.append((time.mktime(each_rev.timestamp_to_datetime().timetuple())))
        return unix_time_list

    def set_x_axis(self, unix_time_list):
        self.x_axis = np.array(unix_time_list)
    
    def plot_graph(self):
        plt.style.use(self.style)

        fig, ax = plt.subplots()

        ax.hist(self.x_axis, bins=8, linewidth=0.5, edgecolor="white")

        ax.set(xlim=(self.x_axis[0], self.x_axis[(len(self.x_axis)-1)]), 
               xticks=np.linspace(self.x_axis[0], self.x_axis[(len(self.x_axis)-1)], 8),
               ylim=(0, 15), yticks=np.linspace(0, 15, 3))
        
        plt.xticks(rotation=45, ha='right')

        plt.show()


if __name__=="__main__":
    article = ArticleHistory("Techno", startyear=2001, endyear=2004)
    Histogram(article)
