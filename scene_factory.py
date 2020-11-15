from scene import Scene
from player import Player
from card import Card
from button_factory import ButtonFactory


class SceneFactory:
    def __init__(self):
        pass

    @staticmethod
    def instantiate_menu():
        # instantiate scene
        menu = Scene()

        button = ButtonFactory.menu_button()
        menu.objects.append(button)

        return menu

    @staticmethod
    def instantiate_game():
        # instantiate scene
        game = Scene()

        player = Player()
        game.objects.append(player)

        card = Card(0)
        game.objects.append(card)

        return game
