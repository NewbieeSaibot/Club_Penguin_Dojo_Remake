from engine.scene import Scene
from game.buttons.menu_play import MenuPlay
from game.buttons.menu_choose_deck import MenuChooseDeck


class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.background = "./game/data/images/backgrounds/The_Fair_2014_Dojo.png"

        button = MenuPlay()
        self.objects.append(button)
        button = MenuChooseDeck()
        self.objects.append(button)
