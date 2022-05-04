from Domain.vector import MyVector
import matplotlib.pyplot as plt


def interpreter_type(type):
    """
    Interpret the way the points will be plot

    Args:
    -----
        @type: int
            the type of the book

    Returns:
    --------
        str
            the shape with which the points will be represented
    """
    if type == 1:
        return "o"
    elif type == 2:
        return "s"
    elif type == 3:
        return "^"
    elif type >= 4:
        return "D"


def verify_color(color):
    """
    Check if a color is valid or not

    Args:
    -----
        @color: str
            color of the vector

    Raises:
    -------
        ValueError
            raised if the color is invalid and is not b(blue), r(red), g(green), y(yellow), m(magenta)

    Returns:
    --------
        bool
            True if color is valid
    """
    if color == "r" or color == "g" or color == "b" or color == "y" or color == "m":
        return True
    else:
        raise ValueError("The color of vector you entered is invalid. Choose one of b(blue), r(red), g(green), "
                         "y(yellow), m(magenta)")


def verify_type(type):
    """
    Check if a type is valid or not

    Args:
    -----
        @type: int
            type of the vector

    Raises:
    -------
        ValueError
            raised if the type is a string or if it is a negative number or 0
    Returns:
    --------
        bool
            True if type is valid
    """
    if isinstance(type, str) or type < 0:
        raise ValueError("The type of vector is invalid. It must be a positive integer greater or equal to 1")
    else:
        return True


def verify_values(values):
    """
        Check if the values are valid or not

        Args:
        -----
            @values: list
                the values of the vector

        Raises:
        -------
            ValueError
                raised if the values are not numbers
        Returns:
        --------
            bool
                True if the values are valid/numbers
        """
    for index in range(len(values)):
        if isinstance(values[index], str):
            raise ValueError("The values must be numbers")
    return True


class VectorRepository:
    """
    Represents a collection of MyVector instances
    """
    def __init__(self, vector_repository=None):
        """
        Constructor of the class. Creates a new collection with MyVector instances

        Args:
        -----

        Keyword args:
        -------------
            @vector_repository
                list of vectors in the collection
        """
        if vector_repository is None:
            vector_repository = []
        self.__vectors = vector_repository.copy()

    def __str__(self):
        """
        Returns:
        --------
            str
                string representation of the current MyVector repository instance
        """
        repr_str = ""
        for element in self.__vectors:
            repr_str += str(element) + "\n"
        repr_str = repr_str.strip()
        return repr_str

    def __len__(self) -> int:
        """
        Overwriting the len() function. With this function implemented we can use len() on any VectorRepository instance
        and it will return the number of vectors in the repository.

        Returns:
        --------
            int
                number of vectors in the repository
       """
        return len(self.__vectors)

    def vector_exists(self, name_id, type, color, values):
        """
    Check if a vector already exists in the repository or not

    Args:
    -----
        @name_id: int or str
            unique identifier of the vector(name of the vector)
        @type: int
            type of the vector
        @color: str
            color of the vector
        @values: list
            numeric values of the vector

    Returns:
    --------
        bool
            False if the vector is no more in the repository, otherwise true
    """
        for index in range(len(self.__vectors)):
            if self.__vectors[index].get_name_id() == name_id and self.__vectors[index].get_type() == type:
                if self.__vectors[index].get_color() == color:
                    if self.__vectors[index].get_values() == values:
                        return True
        return False

    def verify_nameid(self, index_check, name_id):
        """
       Check if a name_id is already used

       Args:
       -----
       @index_check: int
           the index from which the verification starts
       @name_id: int or str
           unique identifier of the vector(name of the vector)

       Returns:
       --------
       int(value_check)
           how many times name_id is used in the repository
        """
        value_check = 0
        for index in range(index_check, -1, -1):
            if self.__vectors[index].get_name_id() == name_id:
                value_check += 1
        return value_check

    def verify_values(self):
        """
       Check if the repository contains valid values or not

       Raises:
       -------
             ValueError
                raised if a name_id is already used
                raised if a color is invalid
                raised if a type is invalid
                raised if the values are invalid
        """
        for index in range(len(self.__vectors)):
            name = self.__vectors[index].get_name_id()
            if self.verify_nameid(index, name) > 1:
                raise ValueError(f"The name_id of vector {index + 1} is already taken/used. Choose another one.")
            else:
                color = self.__vectors[index].get_color()
                if color != "r" and color != "g" and color != "b" and color != "y" and color != "m":
                    raise ValueError(f"The color of vector {index + 1} you entered is invalid. "
                                     f"Choose one of b(blue), r(red), g(green), y(yellow), m(magenta).")
                else:
                    type = self.__vectors[index].get_type()
                    if isinstance(type, str) or type < 1:
                        raise ValueError(f"The type of vector {index + 1} you entered is invalid. "
                                         f"It must be a positive integer greater or equal to 1")
                    else:
                        values = self.__vectors[index].get_values()
                        for element in range(len(values)):
                            if isinstance(values[element], str):
                                raise ValueError(
                                    f"The value at position {element} of the vector {index + 1} is invalid. "
                                    f"It must be a number")
        return True

    def add_vector(self, name_id, color, type, values):
        """
        Add new vector instance to the repository

        Args:
        ----
            @name_id: int or str
                name_id of the vector
            @color: str
                color of the vector
            @type: int
                type of the vector
            @values: list
                numeric values of the vector
        Raises:
        -------
            ValueError
                raised if
        """
        if self.verify_nameid(len(self.__vectors) - 1, name_id) >= 1:
            raise ValueError("The name_id of vector is already taken/used. Choose another one.")

        if not verify_color(color):
            raise ValueError("The color of vector {index+1} you entered is invalid.Choose one of b(blue), r(red), "
                             "g(green), y(yellow), m(magenta).")

        if not verify_type(type):
            raise ValueError("The type of vector is invalid.It must be a positive integer greater or equal to 1")

        if not verify_values(values):
            raise ValueError("The values must be numbers")

        self.__vectors.append(MyVector(name_id, color, type, values))

    def get_vector_at_index(self, index):
        """
        Get the vector at a given index from the repository

        Args:
        -----
            @new_name_id: int or str
                name_id of the vector
            @new_color: str
                color of the vector
            @new_type: int
                type of the vector
            @values: list
                numeric values of the vector

        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository

        Returns:
        --------
            MyVector
                vector instance at the given index
        """
        if 0 <= index < len(self.__vectors):
            return self.__vectors[index]
        else:
            raise IndexError(f"Index should be between 0 and {len(self.__vectors) - 1}")

    def update_vector_by_index(self, index, new_name_id, new_color, new_type, new_values):
        """
        Update the vector at a given index in the repository

        Args:
        -----
            @index: int
            @new_name_id: int or str
                name_id of the vector
            @new_color: str
                color of the vector
            @new_type: int
                type of the vector
            @values: list
                numeric values of the vector

        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository
            ValueError
                raised if a name_id is already used
                raised if a color is invalid
                raised if a type is invalid
                raised if the values are invalid

        Returns:
        --------
            MyVector
                MyVector instance at the given index after update

        """
        if index < 0 or index >= len(self.__vectors):
            raise IndexError(f"Index should be between 0 and {len(self.__vectors) - 1}")

        if self.verify_nameid(len(self.__vectors)-1, new_name_id) > 0:
            raise ValueError("The name_id of vector is already taken/used. Choose another one.")

        if not verify_color(new_color):
            raise ValueError("The color of vector {index+1} you entered is invalid.Choose one of b(blue), r(red), "
                             "g(green), y(yellow), m(magenta).")

        if not verify_type(new_type):
            raise ValueError("The type of vector is invalid.It must be a positive integer greater or equal to 1")

        if not verify_values(new_values):
            raise ValueError("The values must be numbers")

        self.__vectors[index].set_name_id(new_name_id)
        self.__vectors[index].set_color(new_color)
        self.__vectors[index].set_type(new_type)
        self.__vectors[index].set_values(new_values)

        return self.__vectors[index]

    def update_vector_by_nameid(self, name_id, new_color, new_type, new_values):
        """
        Update the vector with a given name_id in the repository

        Args:
        -----
            @name_id: int or str
                name_id of the vector
            @new_color: str
                color of the vector
            @new_type: int
                type of the vector
            @values: list
                numeric values of the vector

        Raises:
        -------
            IndexError
                raised if the name_id does not exist in the repository
            ValueError
                raised if a color is invalid
                raised if a type is invalid
                raised if the values are invalid

        Returns:
        --------
            MyVector
                MyVector instance with the give name_id after update
        """
        if self.verify_nameid(len(self.__vectors)-1, name_id) == 0:
            raise IndexError("The name_id of vector doesnt exist. Choose another one.")

        if not verify_color(new_color):
            raise ValueError("The color of vector {index+1} you entered is invalid.Choose one of b(blue), r(red), "
                             "g(green), y(yellow), m(magenta).")

        if not verify_type(new_type):
            raise ValueError("The type of vector is invalid.It must be a positive integer greater or equal to 1")

        if not verify_values(new_values):
            raise ValueError("The values must be numbers")

        for index in range(len(self.__vectors)):
            if self.__vectors[index].get_name_id() == name_id:
                self.__vectors[index].set_color(new_color)
                self.__vectors[index].set_type(new_type)
                self.__vectors[index].set_values(new_values)
                return self.__vectors[index]

    def delete_vector_by_index(self, the_index):
        """
        Delete the vector at a given index from the repository

        Args:
        -----
            @the_index: int
                the index on which the vector will be deleted

        Raises:
        -------
            IndexError
                raised if the index does not exist in the repository

        Returns:
        --------
            MyVector
                the vector that was deleted
        """

        if the_index < 0 or the_index >= len(self.__vectors):
            raise IndexError(f"Index should be between 0 and {len(self.__vectors) - 1}")
        else:
            copy = self.__vectors[the_index]
            del self.__vectors[the_index]
            return copy

    def delete_vector_by_name_id(self, name_id):
        """
        Delete the vector with a given name_id from the repository

        Args:
        -----
            @name_id: int or str
                the index on which the vector will be deleted

        Raises:
        -------
            IndexError
                raised if the name_id does not exist in the repository

        Returns:
        --------
            MyVector
                the vector that was deleted
        """
        if self.verify_nameid(len(self.__vectors)-1, name_id) == 0:
            raise IndexError("The name_id of vector doesnt exist. Choose another one.")

        for index in range(len(self.__vectors)):
            if self.__vectors[index].get_name_id() == name_id:
                copy = self.__vectors[index]
                del self.__vectors[index]
                return copy

    def plot_vectors(self):
        """
        Plot all vectors in a chart
        """
        for index in range(len(self.__vectors)):
            x = self.__vectors[index].get_values()
            y = interpreter_type(self.__vectors[index].get_type()) + str(self.__vectors[index].get_color())
            plt.plot(x, y)
        plt.show()

    def sum_of_all_elements(self):
        """
        Get the sum of elements in all vectors

        Returns:
        --------
            int
              sum of elements in all vectors
        """
        sums = 0
        for index in range(len(self.__vectors)):
            values = self.__vectors[index].get_values()
            for element in range(len(values)):
                sums += values[element]
        return sums

    def delete_all_vectors(self):
        """
        Delete all vectors from the repository
        """
        self.__vectors.clear()
        return "The repository is empty"

    def update_vectors_by_given_type(self, given_type, given_color):
        """
       Update all vectors having a given type by setting their color to the same given value

       Args:
       -----
            @given_type: int
                the type of vectors that will be updated
            @given_color: str
                the color of the vectors with which it will be updated

        Raises:
        -------
            ValueError
                raised if a color is invalid
                raised if a type is invalid

        Returns:
        --------
            array(int)
                Indices of vectors that have changed
        """

        if not verify_color(given_color):
            raise ValueError("The color of vector {index+1} you entered is invalid.Choose one of b(blue), r(red), "
                             "g(green), y(yellow), m(magenta).")

        if not verify_type(given_type):
            raise ValueError("The type of vector is invalid.It must be a positive integer greater or equal to 1")

        indexes = []
        for index in range(len(self.__vectors)):
            if self.__vectors[index].get_type() == given_type:
                indexes.append(index)
                self.__vectors[index].set_color(given_color)
        return indexes
