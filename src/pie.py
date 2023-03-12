import matplotlib.pyplot as plt
try:
    from src.plot import Plot
    from src.history import History
except ModuleNotFoundError:
    from plot import Plot
    from history import History

class Pie(Plot):
    def __init__(self, history):
        self.history: History = history
        self.graph = self.plot_graph()

    def plot_graph(self):

        fig, ax = plt.subplots(layout="constrained")
        plt.rcParams["figure.constrained_layout.use"] = True

        labels = ('Frogs', 'Hogs', 'Dogs', 'Logs', 'Cogs', 'Mogs', 'Clogs')
        sizes = [95, 95, 95, 10, 10, 10, 10]
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", pctdistance=1.2, labeldistance=1.4)

        fig.suptitle("In development :)")

        ax.plot([1,2,3],[3,2,1])
        plt.xticks(rotation=45)

        return fig