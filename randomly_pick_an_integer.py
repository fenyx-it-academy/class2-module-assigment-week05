'''
Write a program which randomly picks an integer from 1 to 100. Your program should prompt the user for guesses
– if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print how much time the user spend to guess the right answer.
You can assume that the user will enter valid input.
'''

'''
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

bunu dene!!!!
'''
import random
print("Guess a number between 1 and 100. ")
random_comp = random.randint(1, 100)
abc = False
while not abc:
    print("Remember, you can only guess between the numbers 1-100!")
    random_user = int(input("Guess here:"))
    if random_user == random_comp:
        print("You guessed right!!!")
        break
    if random_user > random_comp:
        print("Too high!")
    if random_user < random_comp:
        print("Too low!")

