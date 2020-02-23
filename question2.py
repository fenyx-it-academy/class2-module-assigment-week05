import math #In order to use the module, we first need to import our module.
print("the least common multiple (L.C.M.)")
def lcm(number1,number2):
    return abs(number1*number2) // math.gcd(number1,number2)#Op deze manier berekenen we de lcm van twee getallen op een korte manier.

number1=int(input("enter number1:"))
number2=int(input("enter number1:"))
print("The L.C.M of",number1,"and",number2,"is",lcm(number1,number2))