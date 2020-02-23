import random
import time
start = time.time()
b = random.randint(1,101)
time.time()
while b != True:
    a = int(input('please enter a number : '))
    if b<a:
        print('Please enter a smaller number')
    elif a<b :
        print('Please enter a bigher number')
    elif a==b :
        print('Your guess is right')
        break
stop = time.time()
print(stop-start)