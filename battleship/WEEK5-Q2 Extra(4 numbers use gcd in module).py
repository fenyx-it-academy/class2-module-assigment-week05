'''In this program, you'll learn to find the least common multiple (L.C.M.) of four numbers and display it.(use gcd
 function in module of math )'''
import math     #We define math module for using gcd.
x=int(input("First number:"))    #We take 4 numbers from user
y=int(input("Second number:"))
z=int(input("Third number:"))
t=int(input("Forth number:"))
def lcd(x,y,z,t):   #We define function lcd
    a=math.gcd(x,y)  #We find gcd of x and y (first two numbers).It is varianle a
    k=int(x*y/a)     #And we find lcd of x and y.It is variable k ( from gcd(x,y)*lcd(x,y)=x*y )
    b=math.gcd(z,t)  #We find gcd of z,t (last two numbers).It is variable b
    l=int(z*t/b)     ##And we find lcd of z and t. It is variable l ( from gcd(z,t)*lcd(z,t)=z*t )
    d=math.gcd(k,l)  # And we find gcd of lcd(x,y) and lcd(z,t).It is variable d
    e=int(k*l/d)     #And finally we weill find lcd of k and l.It is variable e .And it is lcd of x,y,z and t
    return int(e)
print("The least common multiple (L.C.M.) of four numbers",lcd(x,y,z,t))
#Finally we print lcd of four numbers
