import random
import time

start_time = time.time()  # We use time function to record the starting time.
random_number = random.randint(1, 100)  # We use random function to get a random number.


def guessing_game():
    while True:  # We use a while loop to continue until the user guesses the number correctly.
        number = int(input('Please enter a number between 1-100: '))  # We take input from the user.
        if number == random_number:  # If the user guesses the number correctly, the program ends.
            print('Congrats! You have guessed the number correctly')
            break
        if abs(number - random_number) <= 5:  # If the difference between the guess and random number is equal to or
            # lower than 5, we warn the user that s/he is close.
            print('It is warm! Try again.')
            # If the difference is higher, then we warn the user that s/he should make a better guess.
        elif abs(number - random_number) > 5 and number > random_number:
            print('Your guess is too high.')
        elif abs(number - random_number) > 5 and number < random_number:
            print('Your guess is too low.')


guessing_game()  # We put the function here to initiate the program.
end_time = time.time()  # # We use time function to record the ending time.
print(f'You have guessed the number in {end_time-start_time:.2f} seconds')  # We print the total time of the program.
