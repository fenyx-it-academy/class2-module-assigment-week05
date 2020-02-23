# We define a function to create the 5*5 board.


def game_board(board):
    print(f'\n{board[1]} {board[2]} {board[3]} {board[4]} {board[5]}\n'
          f'{board[6]} {board[7]} {board[8]} {board[9]} {board[10]}\n'
          f'{board[11]} {board[12]} {board[13]} {board[14]} {board[15]}\n'
          f'{board[16]} {board[17]} {board[18]} {board[19]} {board[20]}\n'
          f'{board[21]} {board[22]} {board[23]} {board[24]} {board[25]}\n')


board = ['|___|'] * 26
