import pygame
from render_able_object import RenderAbleObject
from interact_able_object import InteractAbleObject


class Player(RenderAbleObject, InteractAbleObject):
    def __init__(self, x=50, y=50, width=20, height=20):
        super().__init__(x, y, width, height)

        # Variables
        self.deck = []
        self.hand = []

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.current_pos[0], self.current_pos[1],
                                                   self.SIZE[0], self.SIZE[1]))

    def interact(self, keys, mouse):
        pass
        # Maybe select the card if the click is going to select something or
        # move the character, whatever
