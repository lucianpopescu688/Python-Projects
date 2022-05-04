from Domain.vector import MyVector


print("         Add a scalar")
print(MyVector("Check", "r", 1, [1, 2, 3, 5]).add_scalar_numpy(5))
print(MyVector("Check", "r", 1, []).add_scalar_numpy(5))
print('-' * 100)

print("         Add two vectors")
print(MyVector.add_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.add_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6, 7])))
print(MyVector.add_two_vectors_numpy(MyVector("Check", "r", 1, []), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.add_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [])))
print('-' * 100)

print("         Subtract a scalar")
print(MyVector.subtract_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), 2))

print('-' * 100)

print("         Subtract two vectors")
print(MyVector.subtract_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.subtract_two_vectors_numpy(MyVector("Cher", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6, 7])))
print(MyVector.subtract_two_vectors_numpy(MyVector("Check", "r", 1, []), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.subtract_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [])))
print('-' * 100)

print("         Multiplication by a scalar")
print(MyVector.multiply_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), 2))
print('-' * 100)

print("         Multiplication of two vectors")
print(MyVector.multiply_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.multiply_two_vectors_numpy(MyVector("Cher", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [4, 5, 6, 7])))
print(MyVector.multiply_two_vectors_numpy(MyVector("Check", "r", 1, []), MyVector("Check", "r", 1, [4, 5, 6])))
print(MyVector.multiply_two_vectors_numpy(MyVector("Check", "r", 1, [1, 2, 3]), MyVector("Check", "r", 1, [])))
print('-' * 100)

print("         Sum of elements in a vector")
print(MyVector.sum_of_elements_numpy(MyVector("Check", "r", 1, [1, 2, 3])))
print('-' * 100)

print("         Products of elements in a vector")
print(MyVector.product_of_elements_numpy(MyVector("Check", "r", 1, [2.5321, 2, 3])))
print('-' * 100)

print("         Average of elements in a vector")
print(MyVector.average_numpy(MyVector("Check", "r", 1, [1, 2, 3])))
print('-' * 100)

print("         Minimum of a vector")
print(MyVector.minimum_numpy(MyVector("Check", "r", 1, [1, 2, 3])))
print('-' * 100)

print("         Maximum of a vector")
print(MyVector.maximum_numpy(MyVector("Check", "r", 1, [1, 2, 3])))
print('-' * 100)
