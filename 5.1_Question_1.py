import random
from time import *

print('This program picks a number and you are the player '
      'who is going to guess the number within the shortest time you can.'
      '\nGood luck!!')
number = random.randint(1, 100)
start_time = time()

while True:
    guess = int(input('Please make a guess: '))
    if guess < number:
        print('Your guess is too low!')
    elif guess > number:
        print('Your guess is too high!')
    else:
        break
end_time = time()
sleep(0.5)
print('Congratulations! You found the number within {} seconds.'.format(round(end_time-start_time)))
