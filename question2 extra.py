from math import gcd #In order to use the module, we first need to import our module. and i just imported it to use gcd.
print("the least common multiple (L.C.M.)")
def lcm(num1,num2,num3,num4):
    return abs(num1*num2*num3*num4) // gcd(gcd(num1,num2),gcd(num3,num4))
#Since only two numbers can be found with gcd, we wanted to calculate separately and then calculate the two numbers found with gcd.

num1=int(input("enter 1.number:"))
num2=int(input("enter 2.number:"))
num3=int(input("enter 3.number:"))
num4=int(input("enter 1.number:"))
print("The L.C.M",num1,num2,num3,num4,"is:",lcm(num1,num2,num3,num4))