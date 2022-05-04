number = int(input())


def sums_of_digits(x):
    """
    Calculates the sum of the digits of a number
    """
    sums = 0
    while x != 0:
        sums += x % 10
        x //= 10
    return sums


def check(number):
    """
    Verify if a given number is special
    """
    for element in range(number // 10, number, 1):
        if element + sums_of_digits(element) == number:
            return True
    return False


print(check(number))
