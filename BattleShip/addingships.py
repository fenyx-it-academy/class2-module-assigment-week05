import random


def add_ships(ship_screen):
    """Adds 3x1 and 2x1 size ships separately to the game board."""

    direction_choice = random.choice(["H", "V"])  # chooses the direction of the big ship
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    ship_screen[x][y] = "X"
    if direction_choice == "V":  # after selection of the first coordinate, chooses a direction
        # and then according to x or y coordinates puts the other 2 pieces of the ship
        if x == 0:
            ship_screen[x+1][y], ship_screen[x+2][y] = "X", "X"
        elif x == 4:
            ship_screen[x-1][y], ship_screen[x-2][y] = "X", "X"
        else:
            ship_screen[x+1][y], ship_screen[x-1][y] = "X", "X"
    elif direction_choice == "H":
        if y == 0:
            ship_screen[x][y+1], ship_screen[x][y+2] = "X", "X"
        elif y == 4:
            ship_screen[x][y-1], ship_screen[x][y-2] = "X", "X"
        else:
            ship_screen[x][y-1], ship_screen[x][y+1] = "X", "X"
    main_ship_coordinates = [[a, b] for a in range(5) for b in range(5) if ship_screen[a][b] == "X"]
    #  returns ship coordinates
    banned_coordinates = []  # codes of between 29-34 finds the neighbour coordinates of big ship
    for d in main_ship_coordinates:
        neighbour_coordinates = [[d[0], d[1]+1], [d[0]+1, d[1]], [d[0]-1, d[1]], [d[0], d[1]-1],
                                 [d[0]+1, d[1]+1], [d[0]-1, d[1]-1], [d[0]+1, d[1]-1], [d[0]-1, d[1]+1]]
        for e in neighbour_coordinates:
            if e[0] in range(5) and e[1] in range(5) and e not in banned_coordinates:
                banned_coordinates.append(e)
    while True:
        i = random.randint(0, 4)
        j = random.randint(0, 4)
        if [i, j] in banned_coordinates:
            continue
        else:
            ship_screen[i][j] = "O"
            break
    while True:
        possible_coordinates = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]
        # selects second piece randomly from possible 4
        second_piece = random.choice(possible_coordinates)
        if second_piece[0] in range(5) and second_piece[1] in range(5) and second_piece not in banned_coordinates:
            ship_screen[second_piece[0]][second_piece[1]] = "O"
            break
        else:
            continue
    return ship_screen
