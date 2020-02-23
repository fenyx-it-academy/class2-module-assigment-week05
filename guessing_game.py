import random
import time

start_time=time.time() #süre başlangıcı.
number=random.randrange(1,100) #randrange son sayıyı dahil etmiyor.

while True:
    guess=int(input("Enter your guess: "))
    #sayıyı doğru tahmin edene kadar input alıyoruz.
    if guess == number:
        end_time=time.time()
        print(f"Yes! Game time is {end_time-start_time}")
        #programın başlaması ile bitmesi arasındaki fark, toplam oyun süresini verecek.
        break

    elif guess > number:
        print("Too high!")

    elif guess < number:
        print("Too low!")