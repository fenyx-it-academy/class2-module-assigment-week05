import random#In order to use the module, we first need to import our module.
import time
print(""""*****************
Number Quessing Game
(From 1 to 100)
******************""")
random_number=random.randint(1,100)
right_of_prediction=9
starttime=time.time() #used to find out how long it has come to the end

while True:
    number=int(input("enter number:"))
    if number<random_number:
        print("information is being questioned ...")
        time.sleep(1)#It will make a wait of 1 second, to press the screen.
        print("your number is low")#if the number I guess is bigger than the number assigned
        right_of_prediction-=1#There will be 1 reduction in each number prediction
    elif number>random_number:#if the number I guess is smaller than the number assigned
        print("information is being questioned ...")
        time.sleep(1)
        print("your number is high")
        right_of_prediction -= 1
    else: #when you guess the correct number
        print("information is being questioned ...")
        time.sleep(1)
        print("Congratulations! Number is:", random_number)
        right_of_prediction -= 1

        break

    if right_of_prediction==0:#when my right ends, he will be out of the game.
        print("your right to guess is over")
        break

endtime=time.time()
print("{}second is the time you spend on finding the right answer ".format(endtime-starttime))