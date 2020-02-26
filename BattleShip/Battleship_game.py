from gamefunctions import *
from addingships import *

ship_screen = [["_"]*5 for i in range(5)]
add_ships(ship_screen)  # imported from adding ships
game_screen = [["_"]*5 for j in range(5)]
game_play(ship_screen, game_screen)
