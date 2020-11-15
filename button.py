import pygame
from threading import Thread
from render_able_object import RenderAbleObject
from interact_able_object import InteractAbleObject


class Button(RenderAbleObject, InteractAbleObject):
    def __init__(self, function, cool_down=20, x=100, y=100, width=100, height=30):
        super().__init__(x, y, width, height)
        self.function = function
        self.cool_down = cool_down
        self.cool_down_current = True

    def interact(self, keys, mouse):
        if mouse.get_pressed()[0] and self.is_inside(mouse.get_pos()[0], mouse.get_pos()[1]) and self.cool_down_current:
            self.cool_down_current = False
            self.function()
            timer = Thread(target=self.wait)
            timer.start()

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.current_pos[0], self.current_pos[1],
                                                   self.SIZE[0], self.SIZE[1]))

    def wait(self):
        clock = pygame.time.Clock()
        for i in range(self.cool_down):
            clock.tick(20)
        self.cool_down_current = True
