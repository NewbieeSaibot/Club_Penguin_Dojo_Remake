from game import globals
from engine.button import Button


class MenuPlay(Button):
    def __init__(self):
        super().__init__(self.go_to_game, x=400, width=200, height=60)
        self.image_path = "./game/data/images/buttons/start.png"

    @staticmethod
    def go_to_game():
        globals.active_scene = 1
        globals.scenes[globals.active_scene].initialize_game()
