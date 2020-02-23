'''Write a program which randomly picks an integer from 1 to 100. Your program should prompt the user for guesses –
if the user guesses incorrectly, it should print whether the guess is too high or too low. If the user guesses
correctly, the program should print how much time the user spend to guess the right answer. You can assume that
the user will enter valid input.'''

from time import*  #We use this import for time of guesses
import random      #We use random for rondomly picks an integer from 1 to 100
def takenumber():   #We define function takenumber for take a guese from user
    number_gueses=int(input("Please guess a number:"))
    return number_gueses

random_number=random.randint(1,100)  #We use randint from random module,1 to 100
starttime=time()  #We define start number for beginning of time
while True:       #We se while loop for checking users gueses
    number_gueses=takenumber()
    if number_gueses>random_number:  # contion -1
        print("checking the number")
        sleep(1)  #we wait a little time.we use sleep for this
        print("The guess is too high")
    elif number_gueses<random_number:  #condition-2
        print("checking the number")
        sleep(1)  #Again we wait a little time.
        print("the guess is too low")
    else:                             #condition -3
        print("Right Answer")
        break                         #if it is right ,we break loop.
endtime=time()   #W define endtime
print("Gueses take ",endtime-starttime,"second" )   #And finelly we find how much time the user spend to guess
                                                    #the right answer









