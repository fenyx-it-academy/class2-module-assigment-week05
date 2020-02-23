import time
import random
from Placing_shots import *
from Player_shot import *
from Game_board import *
# We import the necessary built-in and the newly created functions.


def shot_check(location):  # We define a function to check if the user shoots a ship.
    return location in three_d_ship or location in two_d_ship
# I put this function into the main file, since it uses the global variables.


print("""'Welcome to the Battleship Game. 
You will choose locations between 1-25 and try to shoot 2 ships randomly placed on the board.
If you shoot one spot, the ship will sink. If you sink both ships, you will win the game.
You can have maximum 10 shots to sink the ships. Otherwise, you lose the game.\n""")

end_rows = [[5, 6], [10, 11], [15, 16], [20, 21]]  # We define end rows to prevent assignments of ships apart.
row_column = [1, 5]  # We define a list to assign ships horizontally or vertically.
locs = [i for i in range(1, 26)]  # We define a list within the range of all possible locations.
three_d_ship = []  # We define a list to record the location of three dot ship.
two_d_ship = []  # We define a list to record the location of two dot ship.
ships_shot = 0  # We define a counter to track the number of ships that are shot during the game.
shots_limit = []  # We define a list to record the number of total shots to put a limit on it.
two_shot_control = []  # We define two lists to prevent double shots of the ships, since one shot is enough for each.
three_shot_control = []

while True:  # We use a while to loop to make computer to assign three dot ship.
    loc1 = random.randint(2, 25)  # Selects numbers excluding top left corner to make the game less easy.
    three_d = random.choice(row_column)  # Randomly chooses whether the ship is placed vertically/horizontally.
    # The first condition makes sure that selected number is in the given range.
    if loc1 + three_d in locs and loc1 + three_d * 2 in locs:
        # The second condition makes sure that the parts of the ship are not in different rows.
        if [loc1, loc1 + three_d] not in end_rows and [loc1 + three_d, loc1 + three_d * 2] not in end_rows:
            three_d_ship.extend([loc1, loc1 + three_d, loc1 + three_d * 2])
            # If all conditions are met we add the location of the ship to its list.
            break

while True:
    # We have same logic as above except we have another condition to prevent the convergence of two ships.
    loc2 = random.randint(2, 25)
    two_d = random.choice(row_column)
    if loc2 + two_d in locs and [loc2, loc2 + two_d] not in end_rows:
        if loc2 not in three_d_ship and loc2 + two_d not in three_d_ship:
            two_d_ship.extend([loc2, loc2 + two_d])
            break

while len(shots_limit) <= 9:  # We use a while loop that limits the user to have 10 shots.
    game_board(board)  # We first print the empty board.
    location = player_shot(board)  # We ask the user to enter an input.
    placing_shots(board, '|_X_|', location)  # We place the shot.
    shots_limit.append(location)  # We record the shot to its specific list.
    shot_check(location)  # We check if the shot is successful.
    time.sleep(1)

    if shot_check(location):  # If the shot is successful, we check which spot of which ship is shot.
        if location in three_d_ship and len(three_shot_control) == 0:
            # First, we check the three dot ship and if the shot is on its location, we mark the location with X
            # and we reveal the ship. Here, we also check whether the ship is already shot.
            if location == loc1:
                board[loc1] = '|_X_|'
                board[loc1 + three_d] = '|_S_|'
                board[loc1 + three_d * 2] = '|_S_|'
                three_shot_control.append(loc1)
                print('You have shot the three dot ship.')
                ships_shot += 1
            elif location == loc1 + three_d:
                board[loc1] = '|_S_|'
                board[loc1 + three_d] = '|_X_|'
                board[loc1 + three_d * 2] = '|_S_|'
                three_shot_control.append(loc1 + three_d)
                print('You have shot the three dot ship.')
                ships_shot += 1
            elif location == loc1 + three_d * 2:
                board[loc1] = '|_S_|'
                board[loc1 + three_d] = '|_S_|'
                board[loc1 + three_d * 2] = '|_X_|'
                three_shot_control.append(loc1 + three_d * 2)
                print('You have shot the three dot ship.')
                ships_shot += 1
        elif location in two_d_ship:  # We follow the same logic for the two dot ship.
            if location == loc2 and len(two_shot_control) == 0:
                board[loc2] = '|_X_|'
                board[loc2 + two_d] = '|_S_|'
                two_shot_control.append(loc2)
                print('You have shot the two dot ship.')
                ships_shot += 1
            elif location == loc2 + two_d and len(two_shot_control) == 0:
                board[loc2] = '|_S_|'
                board[loc2 + two_d] = '|_X_|'
                two_shot_control.append(loc2 + two_d)
                print('You have shot the two dot ship.')
                ships_shot += 1
        if ships_shot == 2:  # If both ships are shot, the user wins the game.
            game_board(board)
            print('Congratulations! You have won the game!')
            break
    else:  # If both ships are not shot, game continues.
        print('Game continues...')
else:  # If two ships cannot be shot in 10 shots, the user loses the game.
    game_board(board)
    print('You have reached the shots limit and lost the game.')