import pytest
import numpy as np
try:
    from src.plot import Plot
    from src.articlehistory import ArticleHistory
    from src.histogram import Histogram
except ModuleNotFoundError:
    from plot import Plot
    from articlehistory import ArticleHistory
    from histogram import Histogram
'''
def test___init__():
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    hist1 = Histogram(art)
'''
def test_pull_dates_from_history(): #FIX ME
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    hist1 = Histogram(art)
    test_x = hist1.pull_dates_from_history()
    test_y = np.array([19343.68607639, 19343.69016204, 19343.70149306, 19343.70491898,
    19343.72989583, 19343.73712963, 19343.75287037, 19343.7678588,
    19343.77221065, 19343.78038194, 19343.78862269, 19343.79084491,
    19343.79743056, 19343.83229167, 19343.84128472, 19343.85881944,
    19343.86075231, 19343.86498843, 19343.87457176, 19345.71658565,
    19345.72155093, 19345.7265625,  19345.75945602, 19345.76724537,
    19345.77728009, 19345.85319444, 19345.86858796, 19345.87462963,
    19345.89653935, 19345.93493056, 19346.77717593, 19346.78079861,
    19346.78736111, 19346.79318287, 19346.82585648])
    assert np.isclose(test_x, test_y) is True


#def test_set_num_bins():

#def test_plot_graph():

if __name__ == "__main__":
    test___init__()
    test_pull_dates_from_history()