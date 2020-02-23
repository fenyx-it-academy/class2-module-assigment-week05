from Space_check import *


def player_shot(board):  # We define a function to get input from the user.
    location = 0  # At the beginning, we define a value of 0 for the location.
    locations = [i for i in range(1, 26)]  # We define a list for possible locations to check whether input is in range.
    while True:
        location = input('Choose your next position between 1-25: ')
        try:  # The function is executed if the input is in given range and the spot is free.
            location = int(location)
            if location in locations and space_check(board, location):
                return location
        except ValueError:  # We warn the user if the input is not appropriate.
            print('\nPlease enter a valid number into an available space.')
            continue
