import pygame
from render_able_object import RenderAbleObject

id_card = [1, 6, 9, 14, 17, 20, 22, 23, 26, 73, 89, 81, 3, 18, 216, 222, 229, 303, 304, 314, 319, 250, 352, 202, 204,
           305, 15, 13, 312, 218, 220, 29, 90]

name = ['CART SURFER', 'PIZZA CHEF', 'CONSTRUCTION WORKER', 'PET SHOP', 'SKI HILL', 'SOCCER', 'BASEBALL',
        'MANHOLE COVER', 'JACKHAMMER', 'FIREFIGHTER', 'SLED RACING', 'ASTRO-BARRIER', 'SNOWBALL FIGHT',
        'Beach Chair Chilling', 'Iceberg', 'Snowball Fight', 'Pizza Parlor', 'Coffee Machine', 'Dojo Courtyard',
        'Beacon', 'Dojo Sketch', 'Cloud Wave', 'Can of Worms', 'Invisible Ninja Suit', 'Costume Trunk', 'SKI VILLAGE',
        'RESCUE SQUAD', 'Clock Tower', 'Fish Costume', 'The Cove', 'SCUBA DIVING', 'AQUA GRABBER']

element = [0, 0, 0, 2, 2, 2, 1, 1, 1, 0, 1, 2, ]  # Fire 0, Water 1, Snow 2
force = [3, 6, 2, 3, 2, 7, 5, 2, 4, 10, 10, 10, ]
image_path = ['./images/cards/id_card.png']


class Card(RenderAbleObject):
    def __init__(self, card_id, x=0, y=0, width=100, height=200):
        super().__init__(x, y, width, height)
        # Variables
        self.name = name[card_id]
        self.type = element[card_id]
        self.force = force[card_id]
        self.image_path = image_path[card_id]

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.current_pos[0], self.current_pos[1],
                                                   self.SIZE[0], self.SIZE[1]))
