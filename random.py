'''Question 1
Write a program which randomly picks an integer from 1 to 100. 
Your program should prompt the user for guesses – if the user guesses incorrectly, 
it should print whether the guess is too high or too low. If the user guesses correctly, 
the program should print how much time the user spend to guess the right answer. 
You can assume that the user will enter valid input.'''

import random

def number_guessing_game():
    print("Guess a number between {low} and {high}. You have {rounds} rounds to try and guess correctly.".format(low=low, high=high, rounds=rounds))
    number = random.randint(low, high)

    for _ in range(rounds):
        guess = input("Enter an integer: ")

        try:
            integer = int(guess)
            if integer == number:
                print('You won!!!')
                return
            elif integer < number:
                print('Try Higher')
            elif integer > number:
                print('Try Lower')

        except ValueError:
            print("You must enter a valid integer.")

    print("You didn't guess correctly in {rounds} rounds. You lost.".format(rounds=rounds))

number_guessing_game(1, 100, 6)








