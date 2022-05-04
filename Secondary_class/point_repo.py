from Main_class.points_list import MyPoint
import math
import matplotlib.pyplot as plt


class PointRepository:
    def __init__(self, points_list=None):
        if points_list is None:
            points_list = []
        self.__points = points_list.copy()

    def __str__(self):
        """
        Converting a PointRepository object into a string.
        :return:
        """
        repr_str = ""
        for element in self.__points:
            repr_str += str(element) + "\n"
        repr_str = repr_str.strip()
        return repr_str

    def get_number_of_points(self):
        """
        Get the number of points in the repository
        :return:
        """
        return len(self.__points)

    def point_exists(self, point_x, point_y, point_color):
        """
        Verify if a point is already in the list
        :param point_x: the abscissa of the point
        :param point_y: the ordinate of the point
        :param point_color: the color of the point
        :return:
        """
        for i in range(len(self.__points)):
            if self.__points[i].get_coordinateX() == point_x and self.__points[i].get_coordinateY() == point_y:
                if self.__points[i].get_color() == point_color:
                    return True
        return False

    def add_point(self, new_entry: list):
        """
        Add a new point to the repository
        :param new_entry: list containing the abscissa, ordinate and color
        :raises IndexError if point already exists in the repository
        :raises ValueError if the color does not match one of the required colors
        """
        if self.point_exists(new_entry[0], new_entry[1], new_entry[2]):
            raise IndexError("Point already exists in the repository")
        self.__points.append(MyPoint(new_entry[0], new_entry[1], new_entry[2]))

    def get_point(self, index):
        """
        Get the point at a given index
        :param index: index of the point
        :return:Point instance which is at the given index in the repository
        :raises IndexError if index is out of bound
        """
        if 0 <= index < len(self.__points):
            return self.__points[index]
        else:
            raise IndexError(f"Index should be between 0 and {len(self.__points)-1}")
    
    def get_point_distance(self, index):
        """
        Get the coordinates of a point at a given index
        :param index: index of the point
        :return: coordinates of a point
        """
        return self.__points[index].get_coordinateX(), self.__points[index].get_coordinateY()

    def get_points_by_the_color(self, color_check):
        """
        Get points that have a certain color
        :param color_check: the color that the points must have
        :return: new PointRepository containing points that have the given color
        :raises ValueError if the color does not comply with the imposed conditions
        """

        if color_check == "red" or color_check == "green" or color_check == "blue" or color_check == "yellow" or \
           color_check == "magenta":
            color_list = []
            for element in range(len(self.__points)):
                if self.__points[element].get_color() == color_check:
                    color_list.append(
                        (self.__points[element].get_coordinateX(), self.__points[element].get_coordinateY()))
            return PointRepository(color_list)
        else:
            raise ValueError("The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

    def get_points_inside_square(self, xcoord, ycoord, lengt):
        """
        Get points that are inside of a given square
        :param xcoord: abscissa of the up-left corner of the square
        :param ycoord: ordinate of the up-left corner of the square
        :param lengt: the length of the side of the square
        :return: new PointRepository containing points that are inside of a given square
        :raises ValueError if the length of the square is a negative number or 0
        """
        if lengt > 0:
            square_list = []
            left_up_x = xcoord
            left_up_y = ycoord
            left_down_y = ycoord - lengt
            right_up_x = xcoord + lengt

            for element in range(0, len(self.__points)):
                if left_up_x <= self.__points[element].get_coordinateX() <= right_up_x:
                    if left_down_y <= self.__points[element].get_coordinateY() <= left_up_y:
                        square_list.append((self.__points[element].get_coordinateX(),
                                            self.__points[element].get_coordinateY()))
            return PointRepository(square_list)
        else:
            raise ValueError("The length of the square must be a positive number greater than 0")

    def get_minimum_distance_between_two_points(self):
        """
        Get the minimum distance between two points
        :return: new PointRepository which contains the minimum distance and points that determine the minimum distance
        :raises ValueError if there are not at least two points in the repository
        """
        if len(self.__points) > 1:
            distanceX = (self.__points[0].get_coordinateX() - self.__points[1].get_coordinateX()) ** 2
            distanceY = (self.__points[0].get_coordinateY() - self.__points[1].get_coordinateY()) ** 2
            minimum = math.sqrt(distanceX + distanceY)
            distances = []
            for element in range(0, len(self.__points) - 1):
                for i in range(element + 1, len(self.__points)):
                    if element != i:
                        disX = (self.__points[element].get_coordinateX() - self.__points[i].get_coordinateX()) ** 2
                        disY = (self.__points[element].get_coordinateY() - self.__points[i].get_coordinateY()) ** 2
                        distance = math.sqrt(disX + disY)
                        if distance < minimum:
                            distances.clear()
                            distances.append(distance)
                            distances.append(element)
                            distances.append(i)
                            minimum = distance
                        elif distance == minimum:
                            distances.append(distance)
                            distances.append(element)
                            distances.append(i)
            return distances
        else:
            raise ValueError("Need to be at least two points in the repository ")

    def update_a_point(self, the_index, the_x, the_y, the_color):
        """
        Update a point with new characteristics
        :param the_index: the index of the point that will be updated
        :param the_x: the new abscissa of the point
        :param the_y: the new ordinate of the point
        :param the_color: the new color of the point
        :return: the new point after the changes
        :raises ValueError if the point already exists in the repository
        :raises IndexError if the index or color does not meet the required parameters
        """
        if self.point_exists(the_x, the_y, the_color):
            raise ValueError("Point already exists in the repository")
        elif 0 <= the_index < len(self.__points) and (the_color == "red" or the_color == "green" or
                                                      the_color == "blue" or the_color == "yellow" or
                                                      the_color == "magenta"):
            self.__points[the_index].set_coordinateX(the_x)
            self.__points[the_index].set_coordinateY(the_y)
            self.__points[the_index].set_coordinate(the_color)
            return self.__points[the_index]
        elif 0 > the_index or the_index > len(self.__points):
            raise IndexError(f"Index should be between 0 and {len(self.__points) - 1} or "
                             f"the color does not meet the required conditions")

    def delete_a_point(self, the_index):
        """
        Delete a point at a given index
        :param the_index: the index of the point to be deleted
        :raises IndexError if index is out of bound
        """
        if 0 <= the_index < len(self.__points):
            del self.__points[the_index]
        else:
            raise IndexError(f"Index should be between 0 and {len(self.__points) - 1}")

    def delete_points_inside_square(self, xcoord, ycoord, lengt):
        """
        Delete the points that are inside of a given square
        :param xcoord: abscissa of the up-left corner of the square
        :param ycoord: ordinate of the up-left corner of the square
        :param lengt: the length of the side of the square
        :return: points left after deletion
        """
        if lengt > 0:
            left_up_x = xcoord
            left_up_y = ycoord
            left_down_y = ycoord - lengt
            right_up_x = xcoord + lengt
            length = len(self.__points)
            element = 0
            while element < length:
                if left_up_x <= self.__points[element].get_coordinateX() <= right_up_x:
                    if left_down_y <= self.__points[element].get_coordinateY() <= left_up_y:
                        del self.__points[element]
                        element -= 1
                        length -= 1
                element += 1
        else:
            raise ValueError("The length of the square must be a positive number greater than 0")

    def plot_all(self):
        """
        Plot all the points in the repository
        :return:
        """
        x = [point.get_coordinateX() for point in self.__points]
        y = [point.get_coordinateY() for point in self.__points]
        color = [point.get_color() for point in self.__points]
        plt.scatter(x, y, c=color)
        plt.show()

    def get_points_inside_circle(self, center_x, center_y, radius):
        """
        Get the points that are inside of a given circle
        :param center_x: the abscissa of the center of the circle
        :param center_y: the ordinate of the center of the circle
        :param radius: the length of the radius of the circle
        :return: new PointRepository which contains the points that are inside of the given circle
        """
        if radius > 0:
            circle_list = []
            for element in range(0, len(self.__points)):
                distance_x = self.__points[element].get_coordinateX() - center_x
                distance_y = self.__points[element].get_coordinateY() - center_y
                if distance_x ** 2 + distance_y ** 2 < radius ** 2:
                    circle_list.append((self.__points[element].get_coordinateX(),
                                        self.__points[element].get_coordinateY()))
            return PointRepository(circle_list)
        else:
            raise ValueError("The radius of the circle must be a positive number greater than 0")

    def number_points_of_a_color(self, color_check):
        if color_check == "red" or color_check == "green" or color_check == "blue" or color_check == "yellow" or \
           color_check == "magenta":
            color_list = []
            for element in range(len(self.__points)):
                if self.__points[element].get_color() == color_check:
                    color_list.append((self.__points[element].get_coordinateX(),
                                       self.__points[element].get_coordinateY()))
            return len(color_list)
        else:
            raise ValueError("The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

    def shift_points_y(self, distance):
        shift_command = input("In which direction do you want the points to shift(up or down): ")
        if shift_command == "up":
            for element in range(len(self.__points)):
                self.__points[element].set_coordinateY(self.__points[element].get_coordinateY() + distance)
        else:
            for element in range(len(self.__points)):
                self.__points[element].set_coordinateY(self.__points[element].get_coordinateY() - distance)
