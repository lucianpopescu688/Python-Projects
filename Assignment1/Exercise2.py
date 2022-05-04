index = int(input())
def formula(index):
    """
    Determine the value of the element at index in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,...
    """
    element = 0
    while index > 0:
        element += 1
        index -= element
    return element

print(formula(index))

"""
element_1 = 0
while index > 0:
    element_1 += 1
    index -= element_1
print(element_1)
"""

