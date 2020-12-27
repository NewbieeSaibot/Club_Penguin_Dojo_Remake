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
        self.is_selected = False

    def interact(self, keys, mouse):
        if self.interact_able:
            if mouse.get_pressed()[0] and self.is_inside(mouse.get_pos()[0], mouse.get_pos()[1]):
                if self.player is not None:
                    self.cool_down_current = False
                    if self.player.selected_card is not None:
                        self.player.selected_card.is_selected = False

                    self.is_selected = True
                    self.player.selected_card = self
                    timer = Thread(target=self.wait)
                    timer.start()

    def draw(self, window):
        if self.visible is not True:
            return

        if self.image_path is not None:
            if self.image is None:
                image = pygame.image.load(self.image_path)
                self.image = pygame.transform.smoothscale(image, (self.SIZE[0], self.SIZE[1]))

            if not self.is_selected:
                window.blit(self.image, (self.current_pos[0], self.current_pos[1]))
            else:
                window.blit(self.image, (self.current_pos[0], self.current_pos[1] - 20))

    def wait(self):
        clock = pygame.time.Clock()
        for i in range(self.cool_down):
            clock.tick(20)
        self.cool_down_current = True
