from deploy import *


def board_print(board):
    """Prints the board with coloumn and row numbers. """
    print('\n   1 2 3 4 5')
    for i in range(1, 6):
        print('{} '.format(i), ' '.join(board[i-1]))


def battleship_gameplay():
    """This function includes all processes of game battleship."""
    game_board = [['_'] * 5 for i in range(5)]
    deploy_big_ship(game_board)
    deploy_small_ship(game_board)
    print("""Welcome to Battleships game. The rules are below:
    1. There are two ships. 3x1 size battleship and 2x1 size warship.
    2. You have to sank battleship within 15 shots. Sanking battleship is enough to win the game.
    3. Your missed shootings are shown as 'X' and your shots on target are shown as '*'
    4. You have to enter the row and coloumn numbers seperately. For example 11, 51, 23, 34 etc. """)
    users_board = [['_'] * 5 for v in range(5)]
    turn_counter = 1
    battleship_counter = 0
    hit_record = []
    while battleship_counter < 3 and turn_counter < 16:
        board_print(users_board)
        print('\nTurn {}'.format(turn_counter))
        users_input = input('Which coordinate do you want to shot? ')
        if str(users_input).isnumeric() is False:
            print('Only numbers!')
            continue
        shot = list(map(int, str(users_input)))
        if shot[0] not in range(1, 6) or shot[1] not in range(1, 6) or len(shot) > 2:
            print('Control your input!')
            continue
        elif game_board[shot[0] - 1][shot[1] - 1] != 'B' and game_board[shot[0] - 1][shot[1] - 1] != 'W':
            users_board[shot[0] - 1][shot[1] - 1] = 'x'
            print('\nYou overshot! Go on..')
            turn_counter += 1
            continue
        elif game_board[shot[0] - 1][shot[1] - 1] == 'B':
            if shot not in hit_record:
                users_board[shot[0] - 1][shot[1] - 1] = '*'
                hit_record.append(shot)
                print('\nNice shot!')
                battleship_counter += 1
                turn_counter += 1
                continue
            elif shot in hit_record:
                print('\nYou have already hit there!')
                turn_counter += 1
        elif game_board[shot[0] - 1][shot[1] - 1] == 'W':
            if shot not in hit_record:
                users_board[shot[0] - 1][shot[1] - 1] = '*'
                hit_record.append(shot)
                print('\nNice shot!')
                turn_counter += 1
                continue
            elif shot in hit_record:
                print('\nYou have already hit there!')
                turn_counter += 1
    if battleship_counter == 3:
        board_print(users_board)
        print('\nCongratulations!!! You sanked the battleship with {} shots.'.format(turn_counter))
    elif turn_counter == 16:
        board_print(users_board)
        print('\nGame Over. Your ammo is over..')
