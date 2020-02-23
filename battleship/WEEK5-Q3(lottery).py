'''Random Lottery Pick
Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.

Note you must adhere to the following conditions:

Lottery number must be 10 digits long.
All 1000 ticket number must be unique.'''

import random   # We use random module for two lucky tickets
lottery_tickets=[]  #We define a empty list for using in for loop
print("We are creating 100 random lottery tickets")
for i in range(100): #We set for loop for creating 100 tickets
    lottery_tickets.append(random.randrange(1000000000,10000000000))  #We use randrange from random module and add to
winners=random.sample(lottery_tickets,2)                              #list lottery_tickets.And we choose 2 numbers
print("Lucky 2 lottery tickets are:",winners)                         #from list.For this ,we use sample from random m.
#Finally we print luck 2 tickets