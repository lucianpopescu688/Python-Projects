from Main_functions.Functions import *


def test_add():
    """
    Test function add
    :return:
    """
    assert add([10, 20, 30], 40) == [10, 20, 30, 40]
    assert add([45], 55) == [45, 55]
    assert add([], 60) == [60]


def test_insert():
    """
    Test function insert
    :return:
    """
    assert insert([10, 15, 20], 0, 25) == [25, 10, 15, 20]
    assert insert([20, 40, 30], 3, 50) == [20, 40, 30, 50]
    assert insert([60, 70, 92, 78, 21], 1, 78) == [60, 78, 70, 92, 78, 21]


def test_remove_element():
    """
    Test function remove_element
    :return:
    """
    assert remove_element([10, 20, 30], 0) == [20, 30]
    assert remove_element([20, 30, 50, 60], 3) == [20, 30, 50]
    assert remove_element([10, 20, 30, 40], 1) == [10, 30, 40]


def test_remove_sequence():
    """
    Test function remove_sequence
    :return:
    """
    assert remove_sequence([10, 20, 30, 40, 50], 0, 0) == [20, 30, 40, 50]
    assert remove_sequence([10, 20, 30, 40, 50], 0, 4) == []
    assert remove_sequence([10, 20, 30, 40, 50], 0, 3) == [50]


def test_replace_element():
    """
    Test function replace_element
    :return:
    """
    assert replace_element([10, 20, 30, 40], 0, 50) == [50, 20, 30, 40]
    assert replace_element([10, 20, 30, 40, 50], 1, 80) == [10, 80, 30, 40, 50]
    assert replace_element([10, 20, 80], 2, 20) == [10, 20, 20]


def test_get_less():
    """
    Test function get_less
    :return:
    """
    assert get_less([20, 30, 40, 10, 25], 40) == [20, 30, 10, 25]
    assert get_less([10, 30, 20, 40], 50) == [10, 30, 20, 40]
    assert get_less([10, 20, 30], 20) == [10]


def test_sorted_participants():
    """
    Test function sorted_participants
    :return:
    """
    assert sorted_participants([10, 50, 40, 30]) == [50, 40, 30, 10]
    assert sorted_participants([90, 80, 70, 30, 20, 10]) == [90, 80, 70, 30, 20, 10]
    assert sorted_participants([10, 20, 30, 40, 50]) == [50, 40, 30, 20, 10]


def test_sorted_by_value():
    """
    Test function sorted_by_value
    :return:
    """
    assert sorted_by_value([50, 30, 40, 70, 90, 60], 40) == [50, 60, 70, 90]
    assert sorted_by_value([90, 80, 70, 60, 30, 10], 20) == [30, 60, 70, 80, 90]
    assert sorted_by_value([25, 35, 31, 37, 32, 39], 30) == [31, 32, 35, 37, 39]


def test_average_scor():
    """
    Test function average_scor
    :return:
    """
    assert average_scor([10, 20, 30, 50], 0, 1) == 15.0
    assert average_scor([10, 30, 50, 70], 0, 0) == 10
    assert average_scor([50, 60, 25, 25], 0, 3) == 40.0


def test_minimum():
    """
    Test function minimum
    :return:
    """
    assert minimum([10, 20, 30, 50], 0, 3) == 10
    assert minimum([25, 30, 21, 22, 23], 1, 3) == 21
    assert minimum([26, 27, 20], 1, 1) == 27


def test_mul():
    """
    Test function mul
    :return:
    """
    assert mul([20, 30, 40, 60], 30, 0, 3) == [30, 60]
    assert mul([10, 20, 30, 40], 3, 0, 3) == [30]
    assert mul([10, 20, 60], 12, 2, 2) == [60]


def test_filter_mul():
    """
    Test function filter_mul
    :return:
    """
    assert filter_mul([10, 20, 30, 40], 11) == []
    assert filter_mul([10, 20, 30, 40], 8) == [40]
    assert filter_mul([10, 22, 33, 44], 22) == [22, 44]


def test_filter_greater():
    """
    Test function filter_greater
    :return:
    """
    assert filter_greater([10, 20, 40, 60], 50) == [60]
    assert filter_greater([20, 25, 25, 26], 24) == [25, 25, 26]
    assert filter_greater([16, 50, 41, 100], 110) == []


def test_undo():
    """
    Test function undo
    :return:
    """
    assert undo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 2) == [1, 2, 5]
    assert undo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 1) == [1, 2]
    assert undo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 0) == [1]


def test_redo():
    """
    Test function redo
    :return:
    """
    assert redo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 0) == [1]
    assert redo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 1) == [1, 2]
    assert redo(([1], [1, 2], [1, 2, 5], [1, 2, 5, 6]), 2) == [1, 2, 5]


def all_tests():
    """
    Run all tests
    :return:
    """
    test_add()
    test_insert()
    test_remove_element()
    test_remove_sequence()
    test_replace_element()
    test_get_less()
    test_sorted_participants()
    test_sorted_by_value()
    test_average_scor()
    test_minimum()
    test_mul()
    test_filter_mul()
    test_filter_greater()
    test_undo()
    test_redo()
    print("All tests passed!\n")
