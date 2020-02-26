from math import gcd


def least_common_multiple(x, y):

    return (x * y) // gcd(x, y)


print(least_common_multiple(x=int(input('x=')), y=int(input('y='))))
