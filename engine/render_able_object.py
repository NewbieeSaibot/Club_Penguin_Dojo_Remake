import pygame


class RenderAbleObject:
    def __init__(self, x, y, width, height):
        self.INITIAL_POS = [x, y]
        self.SIZE = [width, height]
        self.current_pos = self.INITIAL_POS
        self.image_path = None
        self.image = None
        self.visible = True

    def draw(self, window):
        if self.visible is not True:
            return

        if self.image_path is not None:
            if self.image is None:
                image = pygame.image.load(self.image_path)
                self.image = pygame.transform.smoothscale(image, (self.SIZE[0], self.SIZE[1]))

            window.blit(self.image, (self.current_pos[0], self.current_pos[1]))
