from math import remainder


def get_digit(num, hasil):
    if len(hasil) = []
    if num % 10 < 10:
        return num
    else:
        div = num / 10
        remainder = num % 10
        get_digit(remainder)


print(get_digit(1))
print(get_digit(13))
print(get_digit(69))
print(get_digit(769))
