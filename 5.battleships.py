"""
  As per our request, you are to develop an “battleships” game that is intended 
  to be played between user and computer itself. Also, with the algorithm you create,
  you’re expected to make the computer play the game with reasonable moves rather than random moves.
  The most important of all, we want you to create a program that is built by dividing 
  the game into pieces and building modules and importing the modules.

"""
from battleships_rules import print_rules
from random import randint

print(print_rules())


# Creating a Board
board = [[' ' for x in range(6)] for y in range(6)]


# This function takes the board as a parameter and will display it to the console.
def print_board(board):
    print('B' + ' | '+ '1' + ' | ' + "2" + ' | ' + "3"+ ' | ' + "4" + ' | ' + "5")
    print('----------------------')
    print('1' + ' | ' + board[1][1]+ ' | ' + board[2][1] + ' | ' + board[3][1] + ' | ' + board[4][1] + ' | ' + board[5][1])
    print('----------------------')
    print('2' + ' | ' + board[1][2] + ' | ' + board[2][2] + ' | ' + board[3][2] + ' | ' + board[4][2] + ' | ' + board[5][2])
    print('----------------------')
    print('3' + ' | ' + board[1][3] + ' | ' + board[2][3] + ' | ' + board[3][3] + ' | ' + board[4][3] + ' | ' + board[5][3])
    print('----------------------')
    print('4' + ' | ' + board[1][4] + ' | ' + board[2][4] + ' | ' + board[3][4] + ' | ' + board[4][4] + ' | ' + board[5][4])
    print('----------------------')
    print('5' + ' | ' + board[1][5] + ' | ' + board[2][5] + ' | ' + board[3][5] + ' | ' + board[4][5] + ' | ' + board[5][5])

#defining where the 3 rows ship 
def gen_3_ship_loc(board):
    # generete random row and col
    row3 = randint(1, len(board) - 1)
    col3 = randint(1, len(board[1]) - 1)
    random_rc3 = randint(0,1)

    # generete 3 rows or cols ship that change conditions according to some situations
    if (row3 <= 3 and col3 > 3) or (random_rc3 == 0 and row3 <= 3 and col3 <= 3):
        ship3_list = [[row3, col3],[row3 + 1, col3],[row3 + 2, col3]]
    elif (row3 > 3 and col3 <= 3) or (random_rc3 == 1 and row3 <= 3 and col3 <= 3):
        ship3_list = [[row3, col3],[row3, col3 + 1],[row3, col3 + 2]]
    else:
        if random_rc3 == 0:
            ship3_list = [[row3, col3],[row3 - 1, col3],[row3 - 2, col3]]
        else:
            ship3_list = [[row3, col3],[row3, col3 - 1],[row3, col3 - 2]]

    return ship3_list



#defining where the 2 rows ship 
def gen_2_ship_loc(board):
    # generete random row and col
    row2 = randint(1, len(board) - 1)
    col2 = randint(1, len(board[1]) - 1)
    random_rc2 = randint(0,1)

    # generete 2 rows or cols ship that change conditions according to some situations
    if (row2 <= 4 and col2 > 4) or (random_rc2 == 0 and row2 <= 4 and col2 <= 4):
        ship2_list = [[row2, col2],[row2 + 1, col2]]
    elif (row2 > 4 and col2 <= 4) or (random_rc2 == 1 and row2 <= 4 and col2 <= 4):
        ship2_list = [[row2, col2],[row2, col2 + 1]]
    else:
        if random_rc2 == 0:
            ship2_list = [[row2, col2],[row2 - 1, col2]]
        else:
            ship2_list = [[row2, col2],[row2, col2 - 1]]
            
    return ship2_list

# This function check if there is a same items in 3rows ship with 2rows ship
def chech_ship():
    global gen_3ship, gen_2ship
    gen_3ship = gen_3_ship_loc(board)
    gen_2ship = gen_2_ship_loc(board)
    

    # if there is a same items in 3rows ship with 2rows ship, generete them again
    for i in gen_3ship:
        if i in gen_2ship:
            gen_3_ship_loc(board)
            gen_2_ship_loc(board)
            chech_ship()



def main_func():
    #asking the user for a guess
    for turn in range(10):
        print("\n===============================================")
        print("Turn " + str(turn+1) + " out of 10.\n") 
        
        whl_kon1 = True
        while whl_kon1:
            try:
                guess_row = int(input("Guess Row:"))
                guess_col = int(input("Guess Col:"))
                whl_kon1 = False
            except:
                print("Please enter valid value")

        print("===============================================")
        gues_list = [guess_row, guess_col]
        
        # if the user's right for 3rows-ship, it was sunk!
        if gues_list in gen_3ship:
            print("\n*** Congratulations! You sunk my 3-rows-or-cols battleship! ***\n")
            for i, j in gen_3ship:
                board[i][j] = "Ø"
             
            gen_3ship.clear()

            # if the 2rows-ship has already been sunk, you won the game
            if gen_2ship == []:
                print("**** Congratulations! You won the game ****\n")
                board.clear()
                game_control()
                break
        # if the user's right for 2rows-ship, it was sunk!
        elif gues_list in gen_2ship:
            print("\n** Congratulations! You sunk my 2-rows-or-cols battleship! **\n")
            for i, j in gen_2ship:
                board[i][j] = "Ø" 
            
            gen_2ship.clear()

            # if the 3rows-ship has already been sunk, you won the game
            if gen_3ship == []:
                print("**** Congratulations! You won the game ****\n")
                board.clear()
                game_control()
                break

        else:
        #warning if the guess is out of the board
            if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                print("Oops, that's not even in the ocean.") 
        
            # warning if the guess was already made
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.") 

            # warning if the guess was sunk
            elif(board[guess_row][guess_col] == "Ø"):
                print("You guessed that you sunk already.")

            #if the guess is wrong, mark the point with an X and  again
            else:
                print("You missed my battleship!\n") 
                board[guess_row][guess_col] = "X"
        
        # Print and board again here
        print_board(board)

    #if the user have made 10 tries, it's game over
    if turn >= 9:
        print("\nGame Over :( \n") 
        game_control()




# we want the game to keep running until the user doesn’t want to play anymore,
# so we will create a small while loop in the game_control function.

# this loop is for checking correct y/n input
def game_control():
    whl_kon = True
    while whl_kon:
        answer = input('Do you want to play? (Y/N) : ')
        if answer in ["Y", "y", "yes", "Yes"]:
            global board
            board = [[' ' for x in range(6)] for y in range(6)]
            print('\n********* NEW GAME IS STARTED **********\n')
            print_board(board)
            chech_ship()
            main_func()
            whl_kon = False
        elif answer in ["N", "n", "no", "No"]:
            print("Thanks for The Game!!!")
            break
        else:
            print("Please! To play again (Y), To quit (N)")

game_control()

# THE END