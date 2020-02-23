#for question5
#We created the module we created in the same directory so that it can come when we call it.
# initializing board
board = []

for x in range(5):
    board.append(["O"] * 5)#Because of the range(5), he would give 5 zeros one after another,
    # and I also asked him to give it side by side and multiplied by 5.

def print_board(board):
    for row in board:
        print(" ".join(row))#we removed the commas with join


# starting the game and printing the board
print("Let's play Battleship!")
print_board(board)
