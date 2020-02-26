from math import gcd


def least_common_multiple(a, b, c, d):
    first = (a*d)//gcd(a, d)
    second = (b*c)//gcd(b, c)
    return (first*second)//gcd(first, second)


print(least_common_multiple(a=int(input('a=')), b=int(input('b=')), c=int(input('c=')), d=int(input('d='))))
