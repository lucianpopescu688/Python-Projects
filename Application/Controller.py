from Domain.vector import MyVector
from Infrastructure.VectorRepository import VectorRepository


class VectorController:
    """
    Controller class to reach the logical/domain layer
    """

    def __init__(self, vector_repository: VectorRepository = VectorRepository()):
        """
        Constructor of the class. Creating a new controller

        Args:
        -----

        Keyword args:
        ------------
            @vector_repository: VectorRepository
                vector repository which will ve 'controlled' by the class. Defaults to VectorRepository().
        """
        self.__vector_repository = vector_repository

    def __str__(self) -> str:
        """
        Returns:
        --------
            str
                string representation of the controller
        """
        return str(self.__vector_repository)

    def add_vector(self, name_id, color, type, values):
        """
        Add new vector instance to the repository

        Args:
        ----
            @new_entry
                list which contains name_id, colour, type and values of the vector
        """
        self.__vector_repository.add_vector(name_id, color, type, values)

    def get_repo(self) -> VectorRepository:
        """
        Returns:
        -------
            VectorRepository
                the VectorRepository instance in the current controller
        """
        return self.__vector_repository

    def get_vector_at_index(self, index: int) -> MyVector:
        """
        Get the vector at a given index from the repository

        Args:
        -----
            @index: int

        Returns:
        --------
            MyVector
                vector instance at the given index
        """
        return self.__vector_repository.get_vector_at_index(index)

    def update_vector_by_index(self, index: int, new_name_id: int or str, new_color: str, new_type: int,
                               new_values: list):
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
        """
        self.__vector_repository.update_vector_by_index(index, new_name_id, new_color, new_type, new_values)

    def update_vector_by_name_id(self, name_id: int or str, new_color: str, new_type: int, new_values: list):
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
        """
        self.__vector_repository.update_vector_by_nameid(name_id, new_color, new_type, new_values)

    def delete_vector_by_index(self, the_index: int):
        """
        Delete the vector at a given index from the repository

        Args:
        -----
            @index: int
                the index on which the vector will be deleted
        """
        self.__vector_repository.delete_vector_by_index(the_index)

    def delete_vector_by_name_id(self, name_id: int or str):
        """
        Delete the vector with a given name_id in the repository

        Args:
        -----
            @name_id: int or str
                name_id of the vector
        """
        self.__vector_repository.delete_vector_by_name_id(name_id)

    def plot_vectors(self):
        """
        Plot all vectors in a chart
        """
        self.__vector_repository.plot_vectors()

    def sum_of_all_elements(self):
        """
       Get the sum of elements in all vectors
        """
        self.__vector_repository.sum_of_all_elements()

    def delete_all_vectors(self):
        """
        Delete all vectors from the repository
        """
        self.__vector_repository.clear()

    def update_vectors_by_given_index(self, given_type: int, given_color: str):
        """
       Update all vectors having a given type by setting their color to the same given value

       Args:
       -----
            @given_type: int
                the type of vectors that will be updated
            @given_color: str
                the color of the vectors with which it will be updated
        """
        self.__vector_repository.update_vectors_by_given_type(given_type, given_color)
