import random
import string

i = 0
password = ''
while i < 2:
    password += random.choice(string.digits)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.punctuation)
    i += 1

while len(password) < 10:
    password += random.choice(string.printable)
print(password)
