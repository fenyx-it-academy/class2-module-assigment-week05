import secrets #module called secrets for generating a strong and secure random number.
import string
string_source=string.ascii_letters+ string.digits+ string.punctuation+string.ascii_letters+ string.digits+ string.punctuation
#If we multiplied by 2, it would repeat the same.so we wrote twice separately.
password=secrets.choice(string.ascii_uppercase)
password+=secrets.choice(string.digits)
password+=secrets.choice(string.punctuation)

for i in range(7):#We wrote range (7) to be 10 chacarter long
    password+=secrets.choice(string_source)

characterList=list(password)
secrets.SystemRandom().shuffle(characterList)#we mix the password we created
password="".join(characterList)#we are getting rid of commas and condition
print("Password is",password)

