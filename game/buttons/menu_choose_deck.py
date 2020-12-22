from engine.button import Button
from game import globals


class MenuChooseDeck(Button):

    def __init__(self):
        super().__init__(self.go_to_shop, x=400, y=200, width=200, height=60)
        self.image_path = "./game/data/images/buttons/choose_deck.png"

    @staticmethod
    def go_to_shop():
        globals.active_scene = 2
