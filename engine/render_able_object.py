class RenderAbleObject:
    def __init__(self, x, y, width, height):
        self.INITIAL_POS = [x, y]
        self.SIZE = [width, height]
        self.current_pos = self.INITIAL_POS

    def draw(self, window):
        pass

    def is_inside(self, x, y):
        return self.current_pos[0] + self.SIZE[0] > x > self.current_pos[0] and \
               self.current_pos[1] + self.SIZE[1] > y > self.current_pos[1]
