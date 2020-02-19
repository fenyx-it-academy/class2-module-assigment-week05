"""

Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits, and 2 special symbols

"""

from string import printable, ascii_uppercase, punctuation, digits, ascii_letters
from random import choices

def unique_password():
    """ This function generates a random password """

    password_list = list()
    password = ''.join(choices(digits, k=2) + choices(printable, k=4) + choices(ascii_uppercase, k=2) + choices(punctuation, k=2))
    password_list.append(password)

    return password_list


print(unique_password())


# a different way
from secrets import choice as choice

  
password_list = ascii_letters + digits + punctuation
while True: 
    password = ''.join(choice(password_list) for i in range(10)) 
    if (sum(not i.isalnum() for i in password) >= 2 and sum(i.isupper() for i in password) >= 2 and sum(i.isdigit() for i in password) >= 2): 
        print(password) 
        break


# THE END