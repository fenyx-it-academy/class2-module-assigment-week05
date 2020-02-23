'''
In this program, you'll learn to find the least common multiple (L.C.M.) of four numbers and display it.
(use gcd function in module of math )
'''
from math import gcd
a = []   
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
third_number = int(input("enter third number: "))
fourth_number = int(input("enter fourth number: "))
a.append(first_number)
a.append(second_number)
a.append(third_number)
a.append(fourth_number) 
  
lcm = a[0]
for i in a[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print (lcm)

