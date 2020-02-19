"""
Random Lottery Pick
Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.

Note you must adhere to the following conditions:

Lottery number must be 10 digits long.
All 1000 ticket number must be unique


"""

from random import randrange as rran, sample as samp

# Generate a 100 lottery tickets number which has 10 digits long
#lottery_tickets_list = [[rran(0, 9) for i in range(10)] for j in range(100)]
lottery_tickets_list = samp(range(1000000000,100000000000), k=100)

# pick two lucky tickets from it as a winner
two_lucky_tickets = samp(lottery_tickets_list, k=2)

print(two_lucky_tickets)



# The End