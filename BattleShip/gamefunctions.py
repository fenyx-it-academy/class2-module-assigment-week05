def show_screen(game_screen):
    """Prints the board"""
    print("\n   1 2 3 4 5 ")
    for i in range(1, 6):
        print("{} ".format(i), " ".join(game_screen[i - 1]))


def game_play(ship_screen, game_screen):
    """Runs the game with the rules below"""
    print("""Are you ready for this beautiful game.
    \n***Battleship Game*** """)
    attack_counter = 10
    big_shot = 0
    shot_coordinates = []
    while big_shot < 3 and attack_counter > 0:
        show_screen(game_screen)
        print('\nAttack number {}'.format(attack_counter))
        shot = list(map(int, str(input("Enter the coordinates without a space between them: "))))
        if ship_screen[shot[0] - 1][shot[1] - 1] == "X":
            if shot not in shot_coordinates:
                shot_coordinates.append(shot)
                print("\nNice shot!!")
                game_screen[shot[0] - 1][shot[1] - 1] = "$"
                big_shot += 1
                attack_counter -= 1
            elif shot in shot_coordinates:
                print("\nYou have already shot there!")
                attack_counter -= 1
                continue
        elif ship_screen[shot[0] - 1][shot[1] - 1] == "O":
            if shot not in shot_coordinates:
                shot_coordinates.append(shot)
                print("\nNice shot!!")
                game_screen[shot[0] - 1][shot[1] - 1] = "$"
                attack_counter -= 1
            elif shot in shot_coordinates:
                print("\nYou have already shot there!")
                attack_counter -= 1
                continue
        else:
            game_screen[shot[0] - 1][shot[1] - 1] = "0"
            print('\nYou missed!')
            attack_counter -= 1
            continue
    if big_shot == 3:
        show_screen(game_screen)
        print('Congratulations! You have destroyed the battleship with {} attack'.format(10 - attack_counter))
    elif attack_counter == 0:
        show_screen(game_screen)
        print('Game Over! You lost! Your ammo is over.')
