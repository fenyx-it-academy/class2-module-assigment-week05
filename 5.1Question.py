import random
import time

pc_number = random.randint(1, 100)
start_time = time.time()
while True:
    guess = int(input('What is your guess???'))
    if guess < pc_number:
        print('Your guess is too low..')
        continue
    elif guess > pc_number:
        print('Your guess is too high..')
        continue
    else:
        break
finish_time = time.time()
time.sleep(1)
print('**** You found the number in ', round(finish_time-start_time), ' seconds ****')
