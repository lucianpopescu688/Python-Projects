def create_list():
    """
    Create a list of natural numbers
    Returns the read list
    """
    lista = [int(item) for item in input().split()]
    return lista


def list_to_string(lista):
    """
    Convert the content of the list of integers into string
    Return the string representation
    :return:
    """
    return [str(element) for element in lista]


def add(score_list, value):
    """
    Add a number at the end of the list
    :param score_list: list of scores(naturals)
    :param value: natural number
    :return:
    """
    score_list.append(value)
    return score_list


def insert(score_list, index, value):
    """
    Add a value to a specific index in the list
    :param score_list: list of scores
    :param index: position in the list where the value is added
    :param value: natural number
    :return:
    """
    score_list.insert(index, value)
    return score_list


def remove_element(score_list, index):
    """
     Removes the element at a specific index
    :param score_list: list of scores
    :param index: the position from which the number is deleted
    :return:
    """
    score_list.pop(index)
    return score_list


def remove_sequence(score_list, start_index, finish_index):
    """
    Removes elements between the two given index
    :param score_list: list of scores
    :param start_index: natural number
    :param finish_index: natural number
    :return:
    """
    removal = finish_index - start_index  # removal - stores how many numbers need to be deleted
    if removal == 0:
        score_list.pop(start_index)
    else:
        removal += 1
        while removal != 0:
            score_list.pop(start_index)
            removal -= 1
    return score_list


def replace_element(score_list, index, new_value):
    """
    Replace the number on a position with a new value
    :param score_list: list of scores
    :param index: the position of the number from which it will change
    :param new_value: the value by which the number will change
    :return:
    """
    score_list[index] = new_value
    return score_list


def get_less(score_list, value):
    """
     Get participants with score less than a certain value
    :param score_list: list of scores
    :param value: natural number
    :return:
    """
    sorted = []
    for i in range(len(score_list)):
        if int(score_list[i]) < value:
            sorted.append(score_list[i])
    return sorted


def sorted_participants(score_list):
    """
    Sort participants by their score
    :param score_list: list of scores
    :return:
    """
    score_list.sort(reverse=True)
    return score_list


def sorted_by_value(score_list, value):
    """
    Sort participants with scores higher than a certain value
    :param score_list: list of scores
    :param value: the minimum value that a score cannot have
    :return:
    """
    sortd = []
    for element in range(len(score_list)):
        if int(score_list[element]) > value:
            sortd.append(score_list[element])
    sortd.sort()
    return sortd


def average_scor(score_list, start_index, finish_index):
    """
        Get the average score for participants between the two given index
     :param score_list: list of scores
     :param start_index: the position from which the calculation of the average starts
     :param finish_index: the position at which the calculation of the average stops
        :return:
     """
    sums = 0
    for element in range(start_index, finish_index+1):
        sums += score_list[element]
    if start_index == finish_index:
        return score_list[start_index]
    else:
        sums /= finish_index - start_index + 1
        return sums


def minimum(score_list, start_index, finish_index):
    """
    Get minimum score for participants between the two given index
    :param score_list: list of scores
    :param start_index: the position from which the search for the minimum score begins
    :param finish_index: the position in which the search for the minimum score stops
    :return:
    """
    mins = score_list[start_index]
    for element in range(start_index + 1, finish_index + 1):
        if mins > score_list[element]:
            mins = score_list[element]
    return mins


def mul(score_list, value, start_index, finish_index):
    """
    Get the score of participants between the two given index, which are multiples of value
    :param score_list: list of scores
    :param value: the value by which the scores must be divisible
    :param start_index: the position from which the search for scores that respect the condition begins
    :param finish_index: the position in which the search for scores that respect the condition stops
    :return:
    """
    minime = []
    for element in range(start_index, finish_index + 1):
        if score_list[element] % value == 0:
            minime.append(score_list[element])
    return minime


def filter_mul(score_list, value):
    """
    Remove participants whose score is not divisible by a certain value
    :param score_list: list of scores
    :param value: the value by which the scores must be divisible
    :return:
    """
    for element in range(len(score_list)-1, -1, -1):
        if int(score_list[element]) % value != 0:
            score_list.pop(element)
    return score_list


def filter_greater(score_list, value):
    """
    Remove participants whose score is less than a certain value
    :param score_list: list of scores
    :param value: the minimum value that a score cannot have
    :return:
    """
    for element in range(len(score_list) - 1, -1, -1):
        if int(score_list[element]) < value:
            score_list.pop(element)
    return score_list


def undo(arrays, undo_list):
    return arrays[undo_list]


def redo(arrays, redo_list):
    return arrays[redo_list]


def readfromfile():
    fin = open("input.txt", "r")
    aux = fin.readline()
    aux = aux.split(" ")
    return aux


def writeinfile(list):
    fout = open("output.txt", "w")
    fout.write(str(list))
