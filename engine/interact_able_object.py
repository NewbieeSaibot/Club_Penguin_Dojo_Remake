class InteractAbleObject:
    def __init__(self):
        pass

    def interact(self, keys, mouse):
        pass

    def is_inside(self, x, y):
        return self.current_pos[0] + self.SIZE[0] > x > self.current_pos[0] and \
               self.current_pos[1] + self.SIZE[1] > y > self.current_pos[1]
