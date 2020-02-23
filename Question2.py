import math


def least_common_multiplier(x, y):
    # In math, GCD*LCM = NUM1*NUM2. We use this formula together with GCD function to calculate LCM.
    return (int(x) * int(y)) / math.gcd(int(x), int(y))


while True:  # We use a while loop to get two appropriate numbers from the user.
    num1 = input('Please enter the first number: ')
    num2 = input('Please enter the second number: ')
    if num1 and num2:  # We check whether the inputs are left blank.
        if not num1.isnumeric() or not num2.isnumeric():  # We check whether the entered numbers are numeric.
            print('Please enter valid numbers.')
            continue
        else:
            break
    else:
        print('You cannot leave the input blank.')
        continue

print(least_common_multiplier(num1, num2))
