import random
from time import *

randomValue = random.randint(1, 100)

start_time = time()
while True:
    userValue = int(input('enter a number between 1 and 100'))
    if userValue > randomValue:
        print('your value is to big')
    elif userValue < randomValue:
        print('your value is too small')
    else:
        print('great you find my number')
        break

end_time = time()
print('oyun suresi', end_time - start_time)
