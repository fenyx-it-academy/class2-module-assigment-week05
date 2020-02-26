import math


def least_common_multiple(number1, number2):
    """finds the least common multiple of two numbers"""
    return number1 * number2 // math.gcd(number1, number2)


print(least_common_multiple(3, 5))


def least_common_multiple2(number1, number2, number3, number4):
    """finds the least common multiple of four numbers"""
    return least_common_multiple((number1 * number2 // math.gcd(number1, number2)),
                                 (number3 * number4 // math.gcd(number3, number4)))


print(least_common_multiple2(3, 5, 7, 11))
