class MyPoint:
    def __init__(self, x, y, color):
        self.__coord_x = x
        self.__coord_y = y
        if color == "red" or color == "green" or color == "blue" or color == "yellow" or color == "magenta":
            self.__color = color
        else:
            raise ValueError(f"The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

    def get_coordinateX(self):
        """
        Get the abscissa of the point
        :return: abscissa of the point
        """
        return self.__coord_x

    def get_coordinateY(self):
        """
        Get the ordinate of the point
        :return: ordinate of the point
        """
        return self.__coord_y

    def get_color(self):
        """
        Get the color of the point
        :return: color of the point
        """
        return self.__color

    def set_coordinateX(self, x):
        """
        Set a new abscissa to the point
        :param x: new abscissa of the point
        """
        self.__coord_x = x

    def set_coordinateY(self, y):
        """
        Set new ordinate to the point
        :param y: new ordinate of the point
        """
        self.__coord_y = y

    def set_coordinate(self, color):
        """
        Set a new color to the point
        :param color: new color of the point
        """
        self.__color = color

    def __str__(self):
        """
        Converting a MyPoint object into a string
        :return:
        """
        return f"Point({self.__coord_x}, {self.__coord_y}) of color {self.__color}"
