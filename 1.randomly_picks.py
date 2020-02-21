"""
Write a program which randomly picks an integer from 1 to 100. 
Your program should prompt the user for guesses – if the user guesses incorrectly,
it should print whether the guess is too high or too low. If the user guesses correctly, 
the program should print how much time the user spend to guess the right answer.
You can assume that the user will enter valid input.

"""
from random import randint as ri
from time import time as tm


def inp_user(if_number):
    """ This function prompts inputs of user 
    and invokes chek_pick_and_inp() by using this inputs as an argument """

    global start_time

    if if_number == 1:
        start_time = tm()
        user_num = int(input("Guess an integer number from 1 to 100 correctly : "))
    elif if_number == 2:
        user_num = int(input("Your number is greater than the correct number. Guess again : "))
    elif if_number == 3:
        user_num = int(input("Your number is lesser than the correct number. Guess again : "))
    return chek_pick_and_inp(user_num)



def randomly_pick():
    """ This function randomly picks an integer from 1 to 100 """
    
    pick_num = ri(1, 100)
    return pick_num

# we assign the random pick to a new value
pick = randomly_pick()


def chek_pick_and_inp(user):
    """ This function checks user input and random pick """

    global pick
    if pick == user:
        check_func(False)
        print("Congratulations !!! You guessed the right answer in {} seconds!!!".format(int(end_time - start_time)) ) 
    elif user > pick  :
        return inp_user(2)
    elif user < pick  :
        return inp_user(3)



def check_func(check):
    """ This function checks start of program and end of program """

    if check:
        print("This program will pick a number from 1 to 100. Just guess the number.\
         \nLet's see how many seconds you will find it.\n")
        inp_user(1)
    else:
        global end_time
        end_time = tm()

check_func(True)



# THE END
