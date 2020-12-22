from engine.scene import Scene
from engine.player import Player


class Game(Scene):
    def __init__(self):
        super().__init__()
        self.background = "./game/data/images/backgrounds/empty_dojo.png"

        player = Player()
        self.objects.append(player)
