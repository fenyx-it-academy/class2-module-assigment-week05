"""
The Structure of our game
1.First of all, we created 5 digits from the bottom up and right to the left where our game will be played (we did this with 0 numbers).
2.we then placed our ship in a random place using functions and modules.
3.We asked the user to have two predictions, from right to left and from top to bottom.
4.For this, we gave only 4 chances by specifying the range (4).
5.Whether the prediction will be the same as where the computer is positioning the ship.
6.we wrote our functions controlling it, and accordingly we printed our inputs and prints.
7.After trying 4 rights we finished with the game over.

"""
from random import randint#It means that I will only use randint from the random module.

from board import * #we created a board module ourselves and transferred all the functions inside it with '*'.

# defining where the ship is
def random_row(board):#Here he chooses a layout from top to bottom.
    return randint(0, len(board) - 1)

def random_col(board):#Here he chooses a layout from left to right.
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# asking the user for a guess
for turn in range(4):#For this, we gave only 4 chances by specifying the range (4).
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        # warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")

        # warning if the guess was already made
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")

        # if the guess is wrong, mark the point with an X and start again
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        # Print turn and board again here
    print("Turn " + str(turn + 1) + " out of 4.")
    print_board(board)

# if the user have made 4 tries, it's game over
if turn >= 3:
    print("Game Over")