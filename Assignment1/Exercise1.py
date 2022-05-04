year_2 = int(input())
def control_digit_2(year_2):
    """
    Calculate the control digit of a integer number, summing up its digits until a sum of only one digit is obtained
    """
    control_digit_1 = 0
    if year_2 < 10:
        return year_2
    else:
        while year_2 != 0:
            control_digit_1 += year_2 % 10
            year_2 //= 10
            if control_digit_1 > 9 and year_2 == 0:
                year_2 = control_digit_1
                control_digit_1 = 0
    return control_digit_1

print(control_digit_2(year_2))


"""
year = int(input())
control_digit = 0
if year < 10:
    print(year)
else:
    while year != 0:
        control_digit += year % 10
        year //= 10
        if control_digit > 9 and year == 0:
            year = control_digit
            control_digit = 0
print(control_digit)
"""
