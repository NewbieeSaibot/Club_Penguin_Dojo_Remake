from game.scenes import game, menu, shop

# Constants
MAIN_SCREEN_SIZE = (1000, 632)
GAME_RHYTHM = 65
GAME_NAME = "Penguins' Heart"

# Variables
active_scene = 0
scenes = [menu.Menu(), game.Game(), shop.Shop()]
