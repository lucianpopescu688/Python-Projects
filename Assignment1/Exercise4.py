n = input()
def number(n):
    """
    Form another number from a number's digits found at odd positions
    """
    another_number = 0
    for i in range(0, len(n), 2):
        another_number = another_number * 10 + int(n[i])
    return another_number

print(number(n))


