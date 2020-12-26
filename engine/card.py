from engine.render_able_object import RenderAbleObject
from engine.interact_able_object import InteractAbleObject
from threading import Thread
import pygame


class Card(RenderAbleObject, InteractAbleObject):
    def __init__(self, id_card, name, element, force, image_path, x=0, y=0, width=100, height=150, cool_down=5):
        super().__init__(x, y, width, height)
        # Variables
        self.id_card = id_card
        self.name = name
        self.type = element
        self.force = force
        self.image_path = image_path
        self.image = None
        self.player = None
        self.interact_able = False
        self.cool_down = cool_down
        self.cool_down_current = True

    def interact(self, keys, mouse):
        if self.interact_able:
            if mouse.get_pressed()[0] and self.is_inside(mouse.get_pos()[0], mouse.get_pos()[1]):
                if self.player is not None:
                    self.cool_down_current = False
                    self.player.selected_card = self
                    timer = Thread(target=self.wait)
                    timer.start()

    def wait(self):
        clock = pygame.time.Clock()
        for i in range(self.cool_down):
            clock.tick(20)
        self.cool_down_current = True
