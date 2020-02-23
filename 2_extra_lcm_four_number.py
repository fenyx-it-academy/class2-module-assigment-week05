from math import gcd


def least_common_multiple():
    y = int(input('enter first number:'))
    x = int(input('enter second number:'))
    z = int(input('enter third number:'))
    k = int(input('enter fuorth number:'))
    #     x, y, z, k = [int(x) for x in input("Enter three value: ").split(',')]
    return int(x * y / gcd(x, y)) * int(z * k / gcd(z, k)) / gcd(int(x * y / gcd(x, y)), int(z * k / gcd(z, k)))


print(least_common_multiple())

