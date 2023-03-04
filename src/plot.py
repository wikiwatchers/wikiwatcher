import matplotlib.pyplot as plt
import numpy as np
from history import History

class Plot:

    def __init__(self, history):
        self.history: History = history
        self.style: str = "seaborn-darkgrid" #default?
        # _mpl-gallery = histogram
        # _mpl-gallery-nogrid = pie chart
        self.x = None
        self.title = None
    
    def set_x(self, data): #input parameter could be self.history.anything
        self.x = data
