import pygame
from engine.render_able_object import RenderAbleObject
from engine.interact_able_object import InteractAbleObject


class Scene:

    def __init__(self):
        self.objects = []
        self.background = None
        self.music = None

    def render(self, window):
        if self.background is not None:
            window.blit(pygame.image.load(self.background), (0, 0))

        for i in range(len(self.objects)):
            if isinstance(self.objects[i], RenderAbleObject):
                self.objects[i].draw(window)

    def input_reactions(self):
        keys = pygame.key
        mouse = pygame.mouse

        for i in range(len(self.objects)):
            if i >= len(self.objects):
                break
            if isinstance(self.objects[i], InteractAbleObject):
                if i >= len(self.objects):
                    break
                self.objects[i].interact(keys, mouse)
