import Secondary_class
from Main_class.points_list import *
from Secondary_class.point_repo import PointRepository


def test_add_point():
    """
    Test function add_point
    :return:
    """
    points = PointRepository()
    points.add_point([4, 6, "red"])
    assert points.get_number_of_points() == 1
    assert points == PointRepository([MyPoint(4, 6, "red")])
    try:
        points.add_point([5, 8, "black"])
        assert False
    except ValueError:
        assert True
    assert points.get_number_of_points() == 1
    assert points == PointRepository([MyPoint(4, 6, "red")])

    try:
        points.add_point([2, 7, "white"])
        assert False
    except ValueError:
        assert True
    assert points.get_number_of_points() == 1
    assert points == PointRepository([MyPoint(4, 6, "red")])


def all_tests():
    """
    Run all tests
    :return:
    """
    test_add_point()
    print("All tests passed!\n")
