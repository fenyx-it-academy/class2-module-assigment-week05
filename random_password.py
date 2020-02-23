'''
Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits, and 2 special symbols

'''

import random

llength = 10 
list_list = []
small_letters = 'abcdefghijklmnopqrstuvwxyz'
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
others = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#list_list = small_letters + big_letters + numbers + others
for i in range(2):
    list_list += random.choice(small_letters)
    list_list += random.choice(big_letters)
    list_list += random.choice(numbers)
    list_list += random.choice(others)

password_password = ''
for c in range(llength):
    password_password += random.choice(list_list)
     
print(password_password)

