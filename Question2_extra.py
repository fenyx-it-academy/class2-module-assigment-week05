import math
import functools


def least_common_multiplier(x, y):
    return (int(x) * int(y)) / math.gcd(int(x), int(y))


def lcm_four(*args):
    return functools.reduce(least_common_multiplier, args)
# We use the LCM function from the previous question to find LCM for four numbers. For this purpose, we use args
# parameter and reduce function.


numbers = []  # We define a list to record the numbers.
while True:  # We use a while loop to get four appropriate numbers from the user.
    a = input('Please enter the first number: ')
    b = input('Please enter the second number: ')
    c = input('Please enter the third number: ')
    d = input('Please enter the fourth number: ')
    if a and b and c and d:  # We check whether the inputs are left blank.
        if not a.isnumeric() or not b.isnumeric() or not c.isnumeric() or not d.isnumeric():
            print('Please enter valid numbers.')  # We check whether the entered numbers are numeric.
            continue
        else:
            a = int(a)  # We convert the inputs into integer and add them to our list.
            b = int(b)
            c = int(c)
            d = int(d)
            numbers.extend([a, b, c, d])
            break
    else:
        print('You cannot leave the input blank.')
        continue

print(lcm_four(a, b, c, d))
