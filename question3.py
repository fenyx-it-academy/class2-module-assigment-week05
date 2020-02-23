import random
import time
lottery_number_list=[]
print("Generate a 100 Lottery tickets...")
time.sleep(3)#After waiting for a while I used sleep to explain the winner
for i in range(100):#Range 100 is given because we will create 100 lottery tickets.
    lottery_number_list.append(random.randrange(1000000000,9999999999))#Since 10 digits are required, we want to choose
    # any number between the smallest and largest ten digits.
    # each will also be unique because it will be added to the list separately.

winners=random.sample(lottery_number_list,2)#Our two selected sample numbers are winners
print("two lucky tickets from it as a winner are",winners)
