# We check whether there is available space on the board.
# In this case, the function's output is True if it is blank or there is a ship on the location.


def space_check(board, location):
    return board[location] == '|___|' or board[location] == '|_S_|'
