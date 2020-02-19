"""
In this program, you'll learn to find the least common multiple (L.C.M.) of two numbers and display it.
(use gcd function in module of math )

Question 2 extra
In this program, you'll learn to find the least common multiple (L.C.M.) of four numbers and display it.
(use gcd function in module of math )

"""

from math import gcd
from functools import reduce

def calculate_lcm(num1, num2):
    """ This function find the least common multiple (L.C.M.) of two numbers 
    by using gcd function in module of math"""

    lcm = (num1 * num2) // gcd(num1, num2)
    return lcm

print(calculate_lcm(12,15))


def four_num_lcm(*numbers):
    """ This function find the least common multiple (L.C.M.) of four numbers 
    by using calculate_lcm function 
    which finds lcm of two numbers by using gcd function in module of math"""

    return reduce(calculate_lcm,numbers)


print(four_num_lcm(12,15,60,30))

# The End