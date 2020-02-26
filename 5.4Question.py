# This programme finds a random password which has 10 characters.
# Password contains at least 2 uppercase letters 2 digits 2 symbols.
import string
import random
password = []
for i in range(2):
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_uppercase))
[password.append(chr(random.randint(33, 126))) for j in range(4)]
random.shuffle(password)
print('Your Password : ', *password, sep='')
