import matplotlib.pyplot as plt
import numpy as np
from plot import Plot
from articlehistory import ArticleHistory
from datetime import datetime

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)
        self.set_x_axis() #change me??

        #helper function here, changes all x into date time and then into unix timestamps?

        plt.style.use(self.style)

        fig, ax = plt.subplots()

        ax.hist(self.x_axis, bins=8, linewidth=0.5, edgecolor="white")

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 56), yticks=np.linspace(0, 56, 9))

        plt.show()

    def set_x_axis(self): #input parameter could be self.history.anything
        """set x graphing data to any parameter"""
        for each_rev in self.history.revisions:
            self.x_axis.append(each_rev.timestamp_to_datetime()) #do we want to change this access any data member?

if __name__ == "histogram":
    article = ArticleHistory("Techno")
    Histogram(article)
