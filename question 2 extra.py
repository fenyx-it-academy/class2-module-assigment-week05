import math
import time
print("In this program, you'll learn to find the least common multiple (L.C.M.) of four numbers and display it")
time.sleep(2)
a = int(input('Please enter a number:  '))
b = int(input('Please enter a number:  '))
c = int(input('Please enter a number:  '))
d = int(input('Please enter a number:  '))
print('Calculating...')
time.sleep(5)
x=math.gcd(a,b)
y=math.gcd(c,d)
result=math.gcd(x,y)
print(result)