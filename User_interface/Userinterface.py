import Main_functions.Functions as Cola
MAX_SCORE = 100


def print_menu():
    """
    Prints the commands available
    """
    print("0 - exit program")
    print("1 - print menu")
    print("2 - read the scores list")
    print("3 - print the scores list")
    print("4 - add a score at the end of the list")
    print("5 - add a number to a certain position")
    print("6 - remove the number at a certain position")
    print("7 - remove a sequence determined by two given positions")
    print("8 - replace the score on a position with a new value")
    print("9 - get participants with score less than a certain value")
    print("10 - sort all participants by their score")
    print("11 - sort participants with scores higher than a certain value")
    print("12 - get the average score for participants between the two positions")
    print("13 – get minimum score for participants between the two given index")
    print("14 - get the score of participants between the two given positions, which are multiples of a certain value")
    print("15 - remove participants whose score is not divisible by a certain value")
    print("16 - remove participants whose score is lower than a certain value")
    print("17 - undo the last operation that modified the array")
    print("18 - redo the last operation that modified the array")
    print("19 - read the list of scores from the file <<input.txt>>")
    print("20 - write the list of score in file <<output.txt>>")


def start():
    """
    Starts the user interface
    """
    values_check = 0
    # scores = [10, 20, 30, 40, 50, 60, 70, 90, 100]
    scores = Cola.readfromfile()

    while values_check == 0 or values_check == 1 or values_check == 2:
        if values_check == 0:
            for element in range(len(scores)):
                scores[element] = int(scores[element])
                if not type(scores[element]) is int or scores[element] < 0 or scores[element] > 100:
                    values_check = 1

            if values_check != 1:
                values_check = 2


        elif values_check == 1:
            print('\033[31m'+"ValueError:Values need to be integers between 0 and 100. Check the values from the file ")
            break

        elif values_check == 2:
            arrays = []
            undo_value = 0
            undo_list = 0
            check_undo = 1
            print_menu()
            command = int(input(">>>"))
            while True:  # while command != 0:
                if command == 1:
                    print_menu()

                elif command == 2:
                    scores = Cola.create_list()
                    values_check = 0

                elif command == 3:
                    print(*(Cola.list_to_string(scores)))

                elif command == 4:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value
                    value = int(input("The number you want to add in the list: "))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))
                    Cola.add(scores, value)

                elif command == 5:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value

                    value = int(input("The number you want to add in the list: "))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100. ")
                        value = int(input("The new value is: "))

                    index = int(input("The position in which the number will be added(index of first element is 0)):"))
                    while index < 0 or index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores)-1)
                        index = int(input("The new index is: "))
                    Cola.insert(scores, index, int(value))

                elif command == 6:
                    index = int(input("The position from which the number will be deleted: "))
                    while index < 0 or index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores) - 1)
                        index = int(input("The new index is: "))
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value
                    Cola.remove_element(scores, index)

                elif command == 7:
                    start_index = int(input("The position from which numbers begin to be deleted: "))
                    while start_index < 0 or start_index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores) - 1)
                        start_index = int(input("The new start_index is: "))

                    finish_index = int(input("The position at which the deletion of numbers stops: "))
                    while finish_index < 0 or finish_index > len(scores) - 1 or finish_index < start_index:
                        print("     ValueError:Value need to be integers between", start_index, "and", len(scores) - 1)
                        finish_index = int(input("The new finish_index is: "))
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value
                    Cola.remove_sequence(scores, start_index, finish_index)

                elif command == 8:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value
                    index = int(input("The position from which to change the number: "))
                    while index < 0 or index > len(scores) - 1:
                        print("     ValueError:Index need to be integers between 0 and ", len(scores) - 1)
                        index = int(input("The new index is: "))

                    new_value = int(input("Value that will change: "))
                    while new_value < 0 or new_value > 100:
                        print("     ValueError:New_value need to be integers between 0 and 100")
                        new_value = int(input("The new new_value is: "))
                    Cola.replace_element(scores, index, new_value)

                elif command == 9:
                    value = int(input("The maximum score a participant can have: "))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))
                    print(*(Cola.get_less(scores, value)))

                elif command == 10:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value
                    Cola.sorted_participants(scores)

                elif command == 11:
                    value = int(input("The minimum value of a score, after which the participants will be sorted: "))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))
                    print("The list is:", *(Cola.sorted_by_value(scores, value)))

                elif command == 12:
                    start_index = int(input("The position from which the calculation of the average starts: "))
                    while start_index < 0 or start_index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores) - 1)
                        start_index = int(input("The new start_index is: "))

                    finish_index = int(input("The position at which the deletion of numbers stops: "))
                    while finish_index < 0 or finish_index > len(scores) - 1 or finish_index < start_index:
                        print("     ValueError:Value need to be integers between", start_index, "and", len(scores) - 1)
                        finish_index = int(input("The new finish_index is: "))
                    print("The average score is:", Cola.average_scor(scores, start_index, finish_index))

                elif command == 13:
                    start_index = int(input("The position from which the search for the minimum score begins:"))
                    while start_index < 0 or start_index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores) - 1)
                        start_index = int(input("The new start_index is: "))

                    finish_index = int(input("The position at which the deletion of numbers stops: "))
                    while finish_index < 0 or finish_index > len(scores) - 1 or finish_index < start_index:
                        print("     ValueError:Value need to be integers between", start_index, "and", len(scores) - 1)
                        finish_index = int(input("The new finish_index is: "))
                    print("The minimum score is:", Cola.minimum(scores, start_index, finish_index))

                elif command == 14:
                    value = int(input("The value by which the scores must be divisible:"))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))

                    start_index = int(input("The index from which the search for scores that respect condition begin:"))
                    while start_index < 0 or start_index > len(scores) - 1:
                        print("     ValueError:Value need to be integers between 0 and ", len(scores) - 1)
                        start_index = int(input("The new start_index is: "))

                    finish_index = int(input("The position at which the deletion of numbers stops: "))
                    while finish_index < 0 or finish_index > len(scores) - 1 or finish_index < start_index:
                        print("     ValueError:Value need to be integers between", start_index, "and", len(scores) - 1)
                        finish_index = int(input("The new finish_index is: "))
                    print("Scores that meet the condition are", *(Cola.mul(scores, value, start_index, finish_index)))

                elif command == 15:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value

                    value = int(input("The value by which the scores must be divisible: "))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))
                    Cola.filter_mul(scores, value)

                elif command == 16:
                    arrays.append(Cola.list_to_string(scores))
                    undo_value += 1
                    undo_list = undo_value

                    value = int(input("The minimum value that a score cannot have:"))
                    while value < 0 or value > 100:
                        print("     ValueError:Value need to be integers between 0 and 100")
                        value = int(input("The new value is: "))
                    Cola.filter_greater(scores, value)

                elif command == 17:
                    if check_undo == 1:
                        arrays.append(scores)
                        check_undo += 1

                    if undo_list == 0:
                        print("There are no more operations that changed the array")
                    else:
                        undo_list -= 1
                        scores = (Cola.undo(arrays, undo_list))
                        redo_list = undo_list

                elif command == 18:
                    if redo_list == len(arrays) - 1:
                        scores = (Cola.redo(arrays, undo_list + redo_list + 1))
                    else:
                        redo_list += 1
                        scores = (Cola.redo(arrays, redo_list))
                    if redo_list == undo_value:
                        arrays.clear()
                        redo_list = 0
                        undo_list = 0
                        undo_value = 0
                        check_undo = 1
                        print("There are no more operations that have not changed the array")

                elif command == 19:
                    scores = Cola.readfromfile()

                elif command == 20:
                    for element in range(len(scores)):
                        scores[element] = str(scores[element])
                    Cola.writeinfile(scores)

                elif command == 0:
                    break

                else:
                    print("Command does not exist!\nEnter a new  one.")
                command = int(input(">>> "))
