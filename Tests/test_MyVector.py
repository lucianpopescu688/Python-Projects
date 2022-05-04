from unittest import TestCase
from Domain.vector import MyVector


class TestVector(TestCase):

    def setUp(self):
        self.MyVector = MyVector("0", "y", 1, [1, 2, 3, 4])

    def test_create(self):
        self.assertEqual(self.MyVector.get_name_id(), "0")
        self.assertEqual(self.MyVector.get_color(), "y")
        self.assertEqual(self.MyVector.get_type(), 1)
        self.assertEqual(self.MyVector.get_values(), [1, 2, 3, 4])

        self.assertEqual(str(self.MyVector), "Vector 0 of color y of type 1 with values [1, 2, 3, 4]")

    # test setters
    self.asser