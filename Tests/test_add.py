from Main_functions.Functions import add
from Main_functions.Functions import insert


def run_add_tests():
    test_add_element_appended_when_array_is_empty()
    test_add_element_appended_when_array_is_not_empty()
    test_add_returns_range_error_when_element_less_0
    test_add_returns_range_error_when_element_greater_100()
    test_add_returns_invalid_type_error()
    test_insert_element_appended_when_index_greater_equal_list_size()
    test_insert_element_inserted_when_index_zero_list_not_empty()
    test_insert_element_at_position_when_list_not_empty()
    test_insert_returns_invalid_index_if_negative()
    test_insert_returns_invalid_type_error_if_index_not_int()
    test_insert_returns_range_error_when_element_greater_100()
    test_insert_returns_range_error_when_element_less_0()
    print("Add/Insert tests passed!")


def test_add_element_appended_when_array_is_empty():
    """
    Test function add
    :return:
    """
    list = []
    result = add(list, 60)
    assert result == None
    assert list == [60]


def test_add_element_appended_when_array_is_not_empty():
    """
    Test function add
    :return:
    """
    list = [30, 45, 21]
    result = add(list, 34)
    assert result == None
    assert list == [30, 45, 21, 34]


def test_add_returns_range_error_when_element_greater_100():
    list = []
    result = add(list, 101)
    assert result == "Element is not in the range [0, 100]"


def test_add_returns_range_error_when_element_less_0():
    list = []
    result = add(list, -1)
    assert result == "Element is not in the range [0, 100]"


def test_add_returns_invalid_type_error():
    list = []
    result = add(list, "Not Int")
    assert result == "Provided value is not an integer"


def test_insert_element_appended_when_index_greater_equal_list_size():
    list = []
    result = insert(list, 0, 31)
    assert result == None
    assert list == [31]


def test_insert_element_inserted_when_index_zero_list_not_empty():
    list = [13, 21, 84]
    result = insert(list, 0, 31)
    assert result == None
    assert list == [31, 13, 21, 84]


def test_insert_element_at_position_when_list_not_empty():
    list = [14, 46, 58, 2]
    result = insert(list, 2, 13)
    assert result == None
    assert list == [14, 46, 13, 58, 2]


def test_insert_returns_invalid_index_if_negative():
    list = []
    result = insert(list, -1, 2)
    assert result == "Index cannot be negative"


def test_insert_returns_invalid_type_error_if_index_not_int():
    list = []
    result = insert(list, "Not int", 2)
    assert result == "Provided index is not integer"


def test_insert_returns_range_error_when_element_greater_100():
    list = []
    result = insert(list, 0, 101)
    assert result == "Element is not in the range [0, 100]"


def test_insert_returns_range_error_when_element_less_0():
    list = []
    result = insert(list, 0, -1)
    assert result == "Element is not in the range [0, 100]"