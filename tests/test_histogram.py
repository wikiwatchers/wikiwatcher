"""tests for Histogram class"""
import pytest
import numpy as np
import matplotlib.dates as mdates
try:
    from src.plot import Plot
    from src.articlehistory import ArticleHistory
    from src.histogram import Histogram
except ModuleNotFoundError:
    from plot import Plot
    from articlehistory import ArticleHistory
    from histogram import Histogram

def test_get_x_axis_data():
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2020, startmonth=1, startday=1,
                        endyear=2020, endmonth=1, endday=30)
    plot1 = Histogram(art)
    x_axis = plot1.get_x_axis_data()
    assert isinstance(x_axis, np.ndarray)
    for each in x_axis:
        np.issubdtype(each.dtype, np.datetime64)

def test_set_num_bins():
    """test for set_num_bins"""
    art = ArticleHistory(titles="Cat", startyear=2021, startmonth=2,
                         endyear=2021, endmonth=3)
    hist1 = Histogram(art)
    hist1.set_num_bins()
    assert np.array_equal(hist1.num_bins, [18660, 18661, 18662, 18663, 18664, 18665, 18666, 18667,
                                           18668, 18669, 18670, 18671, 18672, 18673, 18674, 18675,
                                           18676, 18677, 18678, 18679, 18680, 18681, 18682, 18683,
                                           18684, 18685, 18686, 18687])

if __name__ == "__main__":
    test_get_x_axis_data()
    test_set_num_bins()