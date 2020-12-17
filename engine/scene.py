import pygame
from render_able_object import RenderAbleObject
from interact_able_object import InteractAbleObject


class Scene:

    def __init__(self):
        self.objects = []

    def render(self, window):
        for i in range(len(self.objects)):
            if isinstance(self.objects[i], RenderAbleObject):
                self.objects[i].draw(window)

    def input_reactions(self):
        keys = pygame.key
        mouse = pygame.mouse

        for i in range(len(self.objects)):
            if isinstance(self.objects[i], InteractAbleObject):
                self.objects[i].interact(keys, mouse)
