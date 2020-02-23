'''Question 3
Random Lottery Pick
Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.

Note you must adhere to the following conditions:

Lottery number must be 10 digits long.
All 1000 ticket number must be unique.'''

import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range (0,10):
  number = random.randint(1,100)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead 
    number = random.randint(1,100)
  
  #Now that we have a unique number, and we append it to our list.
  lotteryNumbers.append(number)

#Sort the list 
lotteryNumbers.sort()

#Display the list on screen:
print(">>> Today's lottery numbers are: ") 
print(lotteryNumbers)