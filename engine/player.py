from engine.render_able_object import RenderAbleObject
from engine.interact_able_object import InteractAbleObject
from threading import Lock
import random

mutex = Lock()


class Player(RenderAbleObject, InteractAbleObject):
    def __init__(self, x=50, y=50, width=20, height=20):
        super().__init__(x, y, width, height)
        # Variables
        self.deck = []
        self.hand = []
        self.selected_card = None
        self.ai = False

    def interact(self, keys, mouse):
        for i in range(len(self.hand)):
            self.hand[i].interact(keys, mouse)

    def draw(self, window):
        mutex.acquire()
        for i in range(len(self.hand)):
            self.hand[i].draw(window)
        mutex.release()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def take_cards(self, number):
        if len(self.deck) <= number:
            return False

        for i in range(number):
            self.hand.append(self.deck.pop())

        return True
