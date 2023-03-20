"""test for plot base class"""
import pytest
try:
    from src.plot import Plot
    from src.articlehistory import ArticleHistory
except ModuleNotFoundError:
    from plot import Plot
    from articlehistory import ArticleHistory


def test___init__():
    """tests plot class initialization"""
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    plot1 = Plot(art)
    assert plot1.history == art
    assert plot1.graph is None
    assert plot1.x_axis == []
    assert plot1.x_axis_label is None
    assert plot1.y_axis_label is None
    assert plot1.title is None

    art2 = ArticleHistory(titles="Cat", startyear=2021, startmonth=2,
                         endyear=2021, endmonth=3)
    plot2 = Plot(art2)
    assert plot2.history == art2
    assert plot2.graph is None
    assert plot2.x_axis == []
    assert plot2.x_axis_label is None
    assert plot2.y_axis_label is None
    assert plot2.title is None

def test_get_x_axis_data():
    """tests the get_x_axis_data() function"""
    art = ArticleHistory(titles="Techno", user="Rio65trio",
                         startyear=2022, startmonth=12, startday=1,
                        endyear=2022, endmonth=12, endday=30)
    plot1 = Plot(art)
    plot1.x_axis = plot1.get_x_axis_data("timestamp")
    assert isinstance(plot1.x_axis, list)
    assert isinstance(plot1.x_axis[0], str)
    assert len(plot1.x_axis) == 35

    plot2 = Plot(art)
    plot2.x_axis = plot2.get_x_axis_data("size")
    assert isinstance(plot2.x_axis, list)
    assert isinstance(plot2.x_axis[0], int)

    plot3 = Plot(art)
    plot3.x_axis = plot3.get_x_axis_data("tags")
    assert isinstance(plot3.x_axis, list)
    assert isinstance(plot3.x_axis[0], list)

    plot4 = Plot(art)
    plot4.x_axis = plot4.get_x_axis_data("")
    with pytest.raises(KeyError):
        raise KeyError("Revisions do not contain this key")

if __name__ == "__main__":
    test___init__()
    test_set_x_axis_data()
