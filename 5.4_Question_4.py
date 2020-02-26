import random
import string


def random_password():
    password = []
    for i in range(2):
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
    for i in range(4):
        password.append(chr(random.randint(33, 126)))
    random.shuffle(password)
    return password


print('Here is a random password: ', *random_password(), sep='')
