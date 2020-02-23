'''Question 4
Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits, and 2 special symbols'''

import random
import string

def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print ("First Random String ", randomStringwithDigitsAndSymbols() )