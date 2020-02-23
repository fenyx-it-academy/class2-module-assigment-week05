import random
import string
#Generate a random Password
password=[]
def randompassword():
    for i in range(2):
        upper = random.choice(string.ascii_uppercase)
        password.append(upper)
    #print(password)
    for i in range(6):
        lower = random.choice(string.ascii_lowercase)
        password.append(lower)
    for i in range(2):
        num = random.choice(string.digits)
        password.append(num)
    for i in range(2):
        symbol = random.choice(string.punctuation)
        password.append(symbol)
        #characters = upper + lower + num + symbol
        #password=  random.choices(characters,weights=[2,4,4,2],k=10)#bu sekilde kendini tekrarladi

    random.shuffle(password)#eger liste karistirilmazsa kod sirasi hic degismiyor, her zaman once 2 bh sonra kh gibi
    print('Your password : \n ',*password)

randompassword()


