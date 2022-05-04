list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_2 = ["1", "5", "6"]
def number(list, list_2):
    """
    Prints all two-digit numbers that verify that the unit digit of
    the number is equal to the unit digit of the number squared
    """
    values = []
    for i in list:
        for j in list_2:
            values.append(int(i + j))
    return values

print(*number(list, list_2))

"""
for k in range(1, 9):
    for j in list_2:
        print(k * 10 + int(j))
"""