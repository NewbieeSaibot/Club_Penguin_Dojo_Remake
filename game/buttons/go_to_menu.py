from engine.button import Button
from game import globals


class GoToMenu(Button):

    def __init__(self):
        super().__init__(self.go_to_menu, x=800, y=30, width=50, height=50)

    @staticmethod
    def go_to_menu():
        globals.active_scene = 0
