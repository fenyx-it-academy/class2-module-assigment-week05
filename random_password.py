import string
import random

password=[]
password += [random.choice(string.ascii_uppercase) for i in range(2)] #2 upper case letter,
password += [random.choice(string.digits) for i in range(2)] #2 digits,
password += [random.choice(string.punctuation) for i in range(2)] # 2 special symbols,
password += [random.choice(string.printable) for i in range(4)] #kalan 4 karakter ise tüm klavyeden rastgele seçiliyor.

random.shuffle(password) #yukarıdaki listeyi karıştırıyoruz.
password= "".join(password) #düzgün çıktı almak için join ile string haline getiriyoruz.

print(password)