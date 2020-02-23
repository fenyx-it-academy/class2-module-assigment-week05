'''battleships.py As per our request, you are to develop an “ battleships ” game that is intended to be played
between user and computer itself. Also, with the algorithm you create, you’re expected to make the computer play
 the game with reasonable moves rather than random moves. The most important of all, we want you to create a
 program that is built by dividing the game into pieces and building modules and importing the modules.(we want
  5*5 table and 2 ship , one of them 3 dots ship and the other 2 dots ship, the ship destroyed in one hit)'''
from random import randint
from shipModule1 import *
from shipModule2 import *
board = []  # We define empty board list
# We create 5*5 board
for x in range(5):
    board.append(["O"]*5)
#
print("Let's play Battleship!")
print_board(board)
#
# Get random coordinates for ship 1
ship1_row = random_row(board)
ship1_col = random_col(board)
# Get random coordinates for ship 2; try again up to 10 times if they are the same as ship 1
for i in range(5):
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    if (ship2_row !=ship1_row and ship2_col==ship1_col) or (ship2_row==ship1_row and ship2_col!=ship1_col):
        break    #We set condition,bacuse it must not be same coordinate
# Cheat by printing positions (for testing):
# print("ship 1: " + str(ship1_row) + " " + str(ship1_col))
# print("ship 2: " + str(ship2_row) + " " + str(ship2_col))

# set initial "win" status as false; these keep track of which of the two ships have been found
ship1_won = False
ship2_won = False
for turn in range(10): #We have 10 chances for shooting
    # We take user guesses
    print("Turn is:" + str(turn + 1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    # We check to see if user guesses match ship 1 and check to see if ship 1 hasn't already been found
    if (guess_row==ship1_row and guess_col==ship1_col and ship1_won==False):
        print("Congratulations! One ship down!")     #If we sunk one ship,same coordinate
        ship1_won=True
        # We set board space to "B" to show correct guess
        board[guess_row][guess_col] = "B"
        # We declare game over if both ships have been found
        if ship1_won==True and ship2_won==True:   #If we sunk battleship
            print("Congratulations! You sunk both battleships!")
            break
    elif (guess_row==ship2_row and guess_col==ship2_col and ship2_won==False):
        print("Congratulations! One ship down!")   #if we sunk one ship,same coordinate
        ship2_won=True
        board[guess_row][guess_col] = "B"
        if ship1_won == True and ship2_won == True:
            print("Congratulations! You sunk both battleships!")  #We sunk all battleship
            break
    else:
        if turn==9:  #If my chances over
            print("Game Over")
        elif (guess_row<0 or guess_row>len(board[0])-1) or (guess_col<0 or guess_col>len(board[0])-1):
            print("That's not even in the sea.")   #if gueses coordinates are not valid

        elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "B"):
            print("Sorry! You fired in the same coordinate!") #IF we fire same coordinate,warning
        else:
            print("You missed!")  # If it is not true gueses,we write x
            board[guess_row][guess_col]="X"
    turn+=1 #We increase our chances
    print(print_board(board))
    #Finally we print print_board() function because we show our board again.