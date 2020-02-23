'''
Random Lottery Pick
Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.

Note you must adhere to the following conditions:

Lottery number must be 10 digits long.
All 1000 ticket number must be unique.

'''
import random

lottery_tickets= []
print("creating 100 random lottery tickets")
for i in range(100): 
    lottery_tickets.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets, 2)  # random.sample() function to choose more than one item from a list and choosing 2 numbers from 100 numbers
print("Lucky 2 lottery tickets are", winners)