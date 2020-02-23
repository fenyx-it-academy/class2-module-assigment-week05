'''In this program, you'll learn to find the least common multiple (L.C.M.) of two numbers and display it.(use gcd
function in module of math )'''

import math   #We want to use gcd  from math module
x=int(input("First number:"))
y=int(input("Second number:"))   # We take numbers from user
def lcd(x,y):  #We define lcd function.
    a=math.gcd(x,y)  #We find gcd  and equal to a.
    b=(x*y)/a   #product of two numbers than if we devide gcd of two numbers,We will find lcd of numbers.
    return int(b)    #Because  always gcd(x,y)*lcd(x,y)=x*y
print("The least common multiple (L.C.M.) of two numbers is:",lcd(x,y))
#Finally we print l.c.m of numbers
