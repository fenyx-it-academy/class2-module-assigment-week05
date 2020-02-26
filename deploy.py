import random


def deploy_big_ship(pc_board):
    """This function deploys 3x1 size battle ship into a 5x5 board randomly."""

    x1, y1 = random.randint(0, 4), random.randint(0, 4)  # Selects the 1st coordinate randomly
    pc_board[x1][y1] = 'B'
    while True:
        second_piece_pool = [[x1+1, y1], [x1-1, y1], [x1, y1+1], [x1, y1-1]]
        second_piece = random.choice(second_piece_pool)  # Selects the 2nd coordinate randomly from the possible options
        if second_piece[0] in range(5) and second_piece[1] in range(5):
            pc_board[second_piece[0]][second_piece[1]] = 'B'
            x2, y2 = second_piece[0], second_piece[1]
            break
        else:
            continue
    while True:  # According to position of the first 2 pieces selects 3rd coordinate from the possible options randomly
        if x1 == x2:
            x3 = x1
            y3 = random.choice([min(y1, y2)-1, max(y1, y2)+1])
            if y3 in range(5):
                pc_board[x3][y3] = 'B'
                break
            else:
                continue
        elif y1 == y2:
            y3 = y1
            x3 = random.choice([min(x1, x2)-1, max(x1, x2)+1])
            if x3 in range(5):
                pc_board[x3][y3] = 'B'
                break
            else:
                continue
    return pc_board


def deploy_small_ship(pc_board):
    """This function randomly deploys 2x1 battle ship into a 5x5 board which has 3x1 size ship in it.
    The rule is ships can not touch each other vertically, horizontally, and diagonally."""
    coordinates_of_big_ship = [[i, j] for i in range(5) for j in range(5) if pc_board[i][j] == 'B']
    banned_coordinates = []
    for k in coordinates_of_big_ship:  # finds the adjacent coordinates of 3x1`size ship.
        adjacents = [[k[0], k[1] - 1], [k[0], k[1] + 1], [k[0] - 1, k[1]], [k[0] + 1, k[1]], [k[0] + 1, k[1] + 1],
                     [k[0] + 1, k[1] - 1], [k[0] - 1, k[1] + 1],
                     [k[0] - 1, k[1] - 1]]
        for m in adjacents:  # appends in a list only the ones in the board.These are banned for the other ship.
            if m[0] in range(5) and m[1] in range(5) and m not in banned_coordinates:
                banned_coordinates.append(m)
    while True:
        x4, y4 = random.randint(0, 4), random.randint(0, 4)
        if [x4, y4] in banned_coordinates:  # if randomly selected coordinate is in banned list it tries again.
            continue
        else:
            pc_board[x4][y4] = 'W'
            break
    while True:  # Selects the second piece of 2x1 size ship from the options only if it is not in the banned list
        second_piece_pool = [[x4+1, y4], [x4-1, y4], [x4, y4+1], [x4, y4-1]]
        second_piece = random.choice(second_piece_pool)
        if second_piece[0] in range(5) and second_piece[1] in range(5) and second_piece not in banned_coordinates:
            pc_board[second_piece[0]][second_piece[1]] = 'W'
            break
        else:
            continue
    return pc_board
