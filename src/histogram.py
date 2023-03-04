import matplotlib.pyplot as plt
import numpy as np
from plot import Plot

class Histogram(Plot):
    def __init__(self, history):
        super().__init__(history)
        super().set_x(self.history.revisions) #change me??

        plt.style.use(self.style)

        fig, ax = plt.subplots()

        ax.hist(self.x, bins=8, linewidth=0.5, edgecolor="white")

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 56), yticks=np.linspace(0, 56, 9))

        plt.show()

if __name__ == "histogram":
    
