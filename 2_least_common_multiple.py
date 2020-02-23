from math import gcd


def least_common_multiple():
    y = int(input('enter first number:'))
    x = int(input('enter second number:'))
    return x * y / gcd(x, y)


print(least_common_multiple())
