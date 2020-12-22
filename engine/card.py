from engine.render_able_object import RenderAbleObject


class Card(RenderAbleObject):
    def __init__(self, id_card, name, element, force, image_path, x=0, y=0, width=100, height=150):
        super().__init__(x, y, width, height)
        # Variables
        self.id_card = id_card
        self.name = name
        self.type = element
        self.force = force
        self.image_path = image_path
        self.image = None
