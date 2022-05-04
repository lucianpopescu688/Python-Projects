from Secondary_class.point_repo import PointRepository
from Main_class.points_list import MyPoint


def print_menu():
    """
    Print the menu options available in the interface.
    :return:
    """
    print("0 - exit program")
    print("1 - print menu")
    print("2 - print points")
    print("3 - add new point")
    print("4 - get the point at a given index")
    print("5 - get the points of a given color ")
    print("6 - get the points that are inside a given square ")
    print("7 - get the minimum distance between two points")
    print("8 - update a point at a given index")
    print("9 - delete a point by index")
    print("10 - delete all points that are inside a given square")
    print("11 - plot all points in a chart")
    print("12 - get all points that are inside a given circle")
    print("13 - get the number of points of a given color")
    print("14 - shift all points on the y axis")


def start():
    """
    Start the menu type console
    :return:
    """
    print_menu()
    command = input(">>> ")
    points_repository = PointRepository([
        MyPoint(1, 1, "blue"),
        MyPoint(2, 2, "magenta"),
        MyPoint(4, 4, "yellow"),
        MyPoint(6, 6, "red"),
        MyPoint(8, 8, "green"),
        MyPoint(10, 10, "blue"),
        MyPoint(12, 12, "green"),
        MyPoint(-2, -2, "red"),
        MyPoint(-1, -1, "green"),
        MyPoint(14, 14, "blue")
    ])

    while command != "0":
        if command == "1":
            print_menu()

        elif command == "2":
            print(points_repository)

        elif command == "3":
            try:
                new_entry = [int(input("The abscissa of the new point is: ")),
                             int(input("The ordinate of the new point is: ")), input("The color of the new point is: ")]
                points_repository.add_point(new_entry)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
            else:
                print(points_repository)

        elif command == "4":
            index = int(input("The index from which the point will be got is: "))
            try:
                print(points_repository.get_point(index))
            except IndexError as ie:
                print(ie)

        elif command == "5":
            color = input("The color that the points must have is: ")
            try:
                color_repository = points_repository.get_points_by_the_color(color)
            except ValueError as ve:
                print(ve)
            else:
                print(color_repository)

        elif command == "6":
            abscissa = int(input("The abscissa of the upper left corner of the square is: "))
            ordinate = int(input("The ordinate of the upper left corner of the square is: "))
            length_square = int(input("The length of the side of the square is: "))
            try:
                square_repository = points_repository.get_points_inside_square(abscissa, ordinate, length_square)
            except ValueError as ve:
                print(ve)
            else:
                print(square_repository)

        elif command == "7":
            try:
                round_distance = points_repository.get_minimum_distance_between_two_points()
                print("The minimum distance between two points is:", round(round_distance[0], 2), "and is between pts:")
                for element in range(1, len(round_distance) - 1, 3):
                    print("Point", points_repository.get_point_distance(round_distance[element]), "and point",
                          points_repository.get_point_distance(round_distance[element + 1]))
            except ValueError as ve:
                print(ve)

        elif command == "8":
            new_index = int(input("The index of the point to be updated is: "))
            new_abscissa = int(input("The new abscissa of the point is: "))
            new_ordinate = int(input("The new ordinate of the point is: "))
            new_color = input("The new color of the point is: ")
            try:
                print(points_repository.update_a_point(new_index, new_abscissa, new_ordinate, new_color))
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)

        elif command == "9":
            index = int(input("The index of the point to be deleted is: "))
            try:
                points_repository.delete_a_point(index)
            except IndexError as ie:
                print(ie)

        elif command == "10":
            abscissa = int(input("The abscissa of the upper left corner of the square is: "))
            ordinate = int(input("The ordinate of the upper left corner of the square is: "))
            length_square = int(input("The length of the side of the square is: "))
            try:
                points_repository.delete_points_inside_square(abscissa, ordinate, length_square)
            except ValueError as ve:
                print(ve)

        elif command == "11":
            points_repository.plot_all()

        elif command == "12":
            circle_center_x = int(input("The abscissa of the center of circle is: "))
            circle_center_y = int(input("The ordinate of the center of circle is: "))
            circle_radius = int(input("The radius of the circle is: "))
            try:
                circle_repo = points_repository.get_points_inside_circle(circle_center_x, circle_center_y, circle_radius)
                print(circle_repo)
            except ValueError as ve:
                print(ve)

        elif command == "13":
            color = input("The color that the points must have is: ")
            try:
                print(points_repository.number_points_of_a_color(color))
            except ValueError as ve:
                print(ve)

        elif command == "14":
            distance = int(input("The distance by which the points will shift is: "))
            points_repository.shift_points_y(distance)

        else:
            print("Command does not exist!\nEnter a new  one.")
        command = input(">>> ")