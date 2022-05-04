from Domain.vector import MyVector


print("         Add a scalar")
print(MyVector("Check", "r", 1, [1, 2, 3]) + 2)
print(MyVector("Check", "r", 1, []) + 2)
print('-' * 100)

print("         Add two vectors")
print(MyVector("Check", "r", 1, [1, 2, 3]) + MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) + MyVector("Check", "r", 1, [4, 5, 6, 7]))
print(MyVector("Check", "r", 1, []) + MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) + MyVector("Check", "r", 1, []))
print('-' * 100)

print("         Subtract a scalar")
print(MyVector("Check", "r", 1, [1, 2, 3]) - 2)
print('-' * 100)

print("         Subtract two vectors")
print(MyVector("Check", "r", 1, [1, 2, 3]) - MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) - MyVector("Check", "r", 1, [4, 5, 6, 7]))
print(MyVector("Check", "r", 1, []) - MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) - MyVector("Check", "r", 1, []))
print('-' * 100)

print("         Multiplication by a scalar")
print(MyVector("Check", "r", 1, [1, 2, 3]) * 2)
print('-' * 100)

print("         Multiplication of two vectors")
print(MyVector("Check", "r", 1, [1, 2, 3]) * MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) * MyVector("Check", "r", 1, [4, 5, 6, 7]))
print(MyVector("Check", "r", 1, []) * MyVector("Check", "r", 1, [4, 5, 6]))
print(MyVector("Check", "r", 1, [1, 2, 3]) * MyVector("Check", "r", 1, []))
print('-' * 100)

print("         Sum of elements in a vector")
print(MyVector("Check", "y", 1, [1]).sum_of_elements())
print('-' * 100)

print("         Products of elements in a vector")
print(MyVector("Check", "y", 1, [1, 2, 3, 4]).product_of_elements())
print('-' * 100)

print("         Average of elements in a vector")
print(MyVector("Check", "y", 1, [1, 2, 3, 4]).average())
print('-' * 100)

print("         Minimum of a vector")
print(MyVector("Check", "y", 1, [1, -2, 3, 4]).minimum())
print('-' * 100)

print("         Maximum of a vector")
print(MyVector("Check", "r", 1, [1, 2, 3]).maximum())
print('-' * 100)