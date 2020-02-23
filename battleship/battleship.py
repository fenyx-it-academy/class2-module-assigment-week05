import random
import math


def drawBoard(board):
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10] + '|')
    print('|' + board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15] + '|')
    print('|' + board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20] + '|')
    print('|' + board[21] + '|' + board[22] + '|' + board[23] + '|' + board[23] + '|' + board[25] + '|')


board = ['_'] * 26


def ifverofhor():
    if random.randint(0, 1) == 0:
        return 'ver'
    else:
        return 'hor'


def isSpaceFree(board, moves):
    return board[moves] == ' '


border_1 = [1, 2, 3, 4, 5]
border_2 = [5, 10, 15, 20, 25]
border_3 = [1, 6, 11, 16, 21]
border_4 = [21, 22, 23, 24, 25]

while True:
    x = random.randint(1, 25)
    print(x)
    if ifverofhor() == 'ver' and
        for i in range(3):
            board[x] = 'X'
            x += 1
        drawBoard(board)
        break
