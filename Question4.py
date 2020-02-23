import string
import random


def password():
    while True:  # We use a while loop to get 10 characters in total to form a password.
        numbers = [m for m in range(10)]  # We define a list of one digit numbers.
        alpha = [i for i in string.ascii_uppercase]
        # We define a list of alphabetical characters with uppercase.
        special = [j for j in string.punctuation]
        # We define a list of special characters.
        # We randomly generate 3 numbers between 2-6 since we need to have a least two of three character types.
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(2, 6)
        if (a+b+c) != 10:  # The loop continues until we get 3 numbers that make 10 in total.
            continue
        elif (a+b+c) == 10:
            return ''.join(map(str, random.choices(numbers,k=a)+random.choices(alpha,k=b)+random.choices(special,k=c)))
        # As the sum of 3 numbers is equal to 10, we pick characters from each list by choices function based on
        # the numbers we generate and we join them together as a password of 10 characters.


print(f'Your randomly generated password is {password()}')


