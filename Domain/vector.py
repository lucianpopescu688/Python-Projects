import numpy as np


class MyVector:
    def __init__(self, name_id, color, type, values=None):
        if values is None:
            values = []
        self.__name_id = name_id

        if color == "r" or color == "g" or color == "b" or color == "y" or color == "m":
            self.__color = color
        else:
            self.__color = color
            print("The color of vector you entered is invalid. Choose one of b(blue), r(red), g(green), "
                  "y(yellow), m(magenta)")

        if isinstance(type, str) or type < 0:
            self.__type = 0
            print("The type of vector is invalid. It must be a positive integer greater or equal to 1")
        else:
            self.__type = type
        self.__values = values

    def __str__(self):
        return f"Vector {self.__name_id} of color {self.__color} of type {self.__type} with values {self.__values}"

    def get_name_id(self):
        copied_ID = self.__name_id
        return copied_ID

    def get_type(self):
        copied_type = self.__type
        return copied_type

    def get_color(self):
        copied_color = self.__color
        return copied_color

    def get_values(self):
        copied_values = self.__values
        return copied_values

    def set_name_id(self, name):
        copied_name = name
        self.__name_id = copied_name

    def set_type(self, type):
        copied_type = type
        self.__type = copied_type

    def set_color(self, color):
        copied_color = color
        self.__color = copied_color

    def set_values(self, values):
        copied_values = values
        self.__values = copied_values

    def __add__(self, other):
        new_values = self.__values
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        else:
            if isinstance(other, int):
                for index in range(len(new_values)):
                    new_values[index] += other
            if isinstance(other, self.__class__):
                if len(other.__values) == 0:
                    return ValueError("There are not values in the list")
                elif len(self.__values) != len(other.__values):
                    return ValueError("Vectors have different lengths")
                else:
                    for index in range(len(new_values)):
                        new_values[index] += other.__values[index]
            return MyVector(self.__name_id, self.__color, self.__type, new_values)

    def __sub__(self, other):
        new_values = self.__values
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        else:
            if isinstance(other, self.__class__):
                if len(other.__values) == 0:
                    return ValueError("There are not values in the list")
                elif len(self.__values) != len(other.__values):
                    return ValueError("Vectors have different lengths")
                else:
                    for index in range(len(new_values)):
                        new_values[index] -= other.__values[index]
                return MyVector(self.__name_id, self.__color, self.__type, new_values)
            else:
                return ValueError("Operation not supported")

    def __mul__(self, other):
        product = 0
        if len(self.__values) == 0:
            return ValueError("There are not values in the list")
        if isinstance(other, self.__class__):
            if len(other.__values) == 0:
                return ValueError("There are not values in the list")
            elif len(self.__values) != len(other.__values):
                return ValueError("Vectors have different lengths")
            else:
                for index in range(len(self.__values)):
                    product += self.__values[index] * other.__values[index]
            return product
        else:
            return ValueError("Operation not supported")

    def sum_of_elements(self):
        sums = 0
        for index in range(len(self.__values)):
            sums += self.__values[index]
        return sums

    def product_of_elements(self):
        product = 1
        for index in range(len(self.__values)):
            product *= self.__values[index]
        return product

    def average(self):
        sums = 0
        for index in range(len(self.__values)):
            sums += self.__values[index]
        avg = sums / len(self.__values)
        return avg

    def minimum(self):
        minimum = self.__values[0]
        for index in range(1, len(self.__values)):
            if minimum > self.__values[index]:
                minimum = self.__values[index]
        return minimum

    def maximum(self):
        maximum = self.__values[0]
        for index in range(1, len(self.__values)):
            if maximum < self.__values[index]:
                maximum = self.__values[index]
        return maximum

    def add_scalar_numpy(self, scalar):
        new_values = np.array(self.__values)
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        new_values[0:len(new_values)] += scalar
        return new_values

    def add_two_vectors_numpy(self, other):
        new_values = np.array(self.__values)
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        if isinstance(other, int):
            for index in range(len(new_values)):
                new_values[index] += other
        if isinstance(other, self.__class__):
            if len(new_values) == 0:
                return ValueError("There are not values in the list")
            elif len(self.__values) != len(other.__values):
                return ValueError("Vectors have different lengths")
            else:
                new_other = np.array(other.__values)
                new_values = np.add(new_values, new_other)
        return MyVector(self.__name_id, self.__color, self.__type, new_values)

    def subtract_two_vectors_numpy(self, other):
        new_values = np.array(self.__values)
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        else:
            if isinstance(other, self.__class__):
                if len(other.__values) == 0:
                    return ValueError("There are not values in the list")
                elif len(self.__values) != len(other.__values):
                    return ValueError("Vectors have different lengths")
                else:
                    new_other = np.array(other.__values)
                    new_values = np.subtract(new_values, new_other)
                return MyVector(self.__name_id, self.__color, self.__type, new_values)
            else:
                return ValueError("Operation not supported")

    def multiply_two_vectors_numpy(self, other):
        new_values = np.array(self.__values)
        if len(new_values) == 0:
            return ValueError("There are not values in the list")
        if isinstance(other, self.__class__):
            if len(other.__values) == 0:
                return ValueError("There are not values in the list")
            elif len(self.__values) != len(other.__values):
                return ValueError("Vectors have different lengths")
            else:
                new_other = np.array(other.__values)
                new_values = new_values.dot(new_other)
            return new_values
        else:
            return ValueError("Operation not supported")

    def sum_of_elements_numpy(self):
        new_values = np.array(self.__values)
        return np.sum(new_values)

    def product_of_elements_numpy(self):
        new_values = np.array(self.__values)
        return np.prod(new_values)

    def average_numpy(self):
        new_values = np.array(self.__values)
        return np.mean(new_values)

    def minimum_numpy(self):
        new_values = np.array(self.__values)
        return np.min(new_values)

    def maximum_numpy(self):
        new_values = np.array(self.__values)
        return np.max(new_values)



