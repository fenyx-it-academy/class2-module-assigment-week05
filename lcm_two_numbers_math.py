'''
In this program, you'll learn to find the least common multiple (L.C.M.) of two numbers and display it.
(use gcd function in module of math )
'''
import math


def asd(n1, n2):
    # find gcd
    gcd = math.gcd(n1, n2)

    # formula
    result = (n1 * n2) / gcd
    return result


n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

lcm = asd(n1, n2)
print("LCM of", n1, "and", n2, "is", "  =  ", lcm)
