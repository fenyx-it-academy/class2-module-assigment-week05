'''Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits, and 2 special symbols
'''
import random  #We use random module for choosing
digits=[0,1,2,3,4,5,6,7,8,9]  #We define all digits in list
upper_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"",t","u","v","w","x","y","z"]
s="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
special=list(s)
#And we define upper,lower letters and special in lists
def randomPassword():  #we define fuction randomPassword
    password=[]        #We have a empty lsit for putting all choosing
    allmix=list(digits+upper_letters+lower_letters+special)  # We define variable all mix for all choices
    password+=random.sample(digits,k=2)#We choose 2 numbers from digits,using sample from random module and add to list
    password+=random.sample(upper_letters,k=2) #We choose 2 upper letters,using sample and add to list
    password+=random.sample(special,k=2)       #We choose 2 special,using sample and add to list
    password += random.sample(allmix,k=4) #For Another choice ,We choose 4 from allmix list, using sample and add list
    random.shuffle(password)              #Finally we shuffle the password
    return password
print ("Random password is:",*randomPassword())
#Finally we print random password

