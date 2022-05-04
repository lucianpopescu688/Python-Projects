from Domain.vector import MyVector
from Infrastructure.VectorRepository import VectorRepository
from Application.Controller import VectorController


def print_menu():
    """
    Print the menu options available in the interface.
    :return:
    """
    print("0 - exit program")
    print("1 - print menu")
    print("2 - print vectors")
    print("3 - add a new vector")
    print("4 - get the vector at a given index")
    print("5 - update a vector at a given index")
    print("6 - update a vector at a given name_id")
    print("7 - delete a vector at a given index")
    print("8 - delete a vector at a given name_id")
    print("9 - plot vectors in a chart")
    print("10 - get the sum of elements in all vectors")
    print("11 - delete all vectors from the repository")
    print("12 - update the vectors having a given type by setting same given color ")


def run(controller: VectorController):
    """
    Start the menu type console
    :return:
    """
    controller = VectorRepository([
        MyVector("0", "y", 1, [4, 5, 6, 7]),
        MyVector("1", "y", 1, [4, 3, 2, 1]),
        MyVector("2", "y", 2, [-4, -3, -2, -1]),
        MyVector("3", "r", 2, [-5, -6, -7, 0]),
        MyVector("4", "g", 3, [-9, -10, -11, -12]),
        MyVector("5", "b", 3, [9, 10, 11, 12]),
        MyVector("6", "g", 4, [-13, -14, -15, -16]),
        MyVector("7", "r", 4, [13, 14, 15, 16]),
        MyVector("8", "g", 1, [17, 18, 19, 20]),
        MyVector("9", "g", 2, [-17, -18, -17, -18])
    ])

    try:
        controller.verify_values()
        print_menu()
        command = input(">>> ")

        while command != "0":
            if command == "1":
                print_menu()

            elif command == "2":
                if len(controller) == 0:
                    print("The Repository is empty")
                else:
                    print(controller)

            elif command == "3":
                try:
                    name_id = input("The name_id of the new vector is: ")
                    color = input("The color of the new vector is: ")
                    type = int(input("The type of the new vector is: "))
                    values = [int(item) for item in input("The values of the vector is: ").split()]
                    controller.add_vector(name_id, color, type, values)
                except ValueError as ve:
                    print(ve)
                else:
                    print(controller)

            elif command == "4":
                try:
                    index = int(input("The index from which the vector will be got is: "))
                    print(controller.get_vector_at_index(index))
                except IndexError as ie:
                    print(ie)

            elif command == "5":
                index = int(input("The index of the vector to be updated is: "))
                new_name_id = input("The new name_id of the vector is: ")
                new_color = input("The new color of the vector is: ")
                new_type = int(input("The new type of the vector is: "))
                new_values = [int(item) for item in input("The new values of the vector is: ").split()]
                try:
                    print(controller.update_vector_by_index(index, new_name_id, new_color, new_type, new_values))
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)

            elif command == "6":
                name_id = input("The name_id of the vector to be updated is: ")
                new_color = input("The new color of the vector is: ")
                new_type = int(input("The new type of the vector is: "))
                new_values = [int(item) for item in input("The new values of the vector is: ").split()]
                try:
                    print(controller.update_vector_by_nameid(name_id, new_color, new_type, new_values))
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)

            elif command == "7":
                index = int(input("The index of the vector to be deleted is: "))
                try:
                    print("The deleted vector is:", controller.delete_vector_by_index(index))
                except IndexError as ie:
                    print(ie)

            elif command == "8":
                name_id = input("The name_id of the vector to be deleted is: ")
                try:
                    print("The deleted vector is:", controller.delete_vector_by_name_id(name_id))
                except IndexError as ie:
                    print(ie)

            elif command == "9":
                controller.plot_vectors()

            elif command == "10":
                print(controller.sum_of_all_elements())

            elif command == "11":
                print(controller.delete_all_vectors())

            elif command == "12":
                given_type = int(input("The type by which the vectors will be updated is: "))
                same_color = input("The color that the vectors will have is: ")
                try:
                    print(controller.update_vectors_by_given_type(given_type, same_color))
                except ValueError as ve:
                    print(ve)
            else:
                print("Command does not exist!\nEnter a new  one.")
            command = input(">>> ")

    except ValueError as ve:
        print(ve)


