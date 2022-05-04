from Application.Controller import VectorController
from Infrastructure.VectorRepository import VectorRepository
from Domain.vector import MyVector

if __name__ == "__main__":
    controller = VectorController(VectorRepository([
        MyVector("0", "y", 1, [4, 5, 6, 7]),
        MyVector("1", "y", 1, [4, 5, 6, 7]),
        MyVector("2", "y", 2, [-4, -3, -2, -1])
    ]))
    print("LIST OF VECTORS:")
    print(controller)
    print("-" * 100)

    controller.add_vector(11, "y", 1, [1, 4, 6])
    print("AFTER ADDING A NEW VECTOR")
    print(controller)
    print("-" * 100)

    print("VECTOR AT INDEX 2:", controller.get_vector_at_index(2))
    print("-" * 100)

    controller.update_vector_by_index(3, 3, "r", 2, [1, 1, 1, 1])
    print("AFTER UPDATE 3TH INDEX:", controller.get_vector_at_index(3))
    print("-" * 100)

    controller.update_vector_by_name_id(3, "y", 5, [2, 2, 2, 2])
    print("AFTER UPDATE VECTOR WITH NAME_ID '3':", controller.get_vector_at_index(3))
    print("-" * 100)

    print("CURRENT STATE OF THE LIST:")
    print(controller)
    controller.delete_vector_by_index(3)
    print("AFTER DELETING ELEMENT AT INDEX 3:")
    print(controller)
    print("-" * 100)

    print("CURRENT STATE OF THE LIST:")
    print(controller)
    controller.delete_vector_by_name_id("0")
    print("AFTER DELETING ELEMENT WITH NAME_ID '0':")
    print(controller)
    print("-" * 100)

    controller.add_vector(11, "y", 1, [1, 4, 6])
    print("AFTER ADDING A NEW VECTOR")
    print(controller)
    print("-" * 100)

    print("CURRENT STATE OF THE LIST:")
    print(controller)
    controller.delete_vector_by_name_id("1")
    print("AFTER DELETING ELEMENT WITH NAME_ID '1':")
    print(controller)
    print("-" * 100)

    print("VECTOR AT INDEX 0:", controller.get_vector_at_index(0))
    print("-" * 100)

    print("LIST OF VECTORS:")
    print(controller)
    print("-" * 100)
