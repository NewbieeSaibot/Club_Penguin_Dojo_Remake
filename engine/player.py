from engine.render_able_object import RenderAbleObject
from engine.interact_able_object import InteractAbleObject


class Player(RenderAbleObject, InteractAbleObject):
    def __init__(self, x=50, y=50, width=20, height=20):
        super().__init__(x, y, width, height)

        # Variables
        self.deck = []
        self.hand = []

    def interact(self, keys, mouse):
        pass
        # Maybe select the card if the click is going to select something or
        # move the character, whatever
