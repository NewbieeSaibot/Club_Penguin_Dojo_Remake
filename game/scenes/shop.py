from engine.scene import Scene
from game.card_factory import CardFactory, cards
from engine.render_able_object import RenderAbleObject
from game.buttons.next_page import NextPage
from game.buttons.last_page import LastPage
from engine.card import Card
from game.buttons.go_to_menu import GoToMenu


class Shop(Scene):
    def __init__(self):
        super().__init__()
        self.page = 0
        self.total_pages = len(cards)//10
        self.instantiated_pages = []
        self.background = "./game/data/images/backgrounds/empty_dojo.png"

        shop_table = RenderAbleObject(x=130, y=30, width=740, height=550)
        shop_table.image_path = "./game/data/images/shop/full_table.png"
        self.objects.append(shop_table)

        button = GoToMenu()
        self.objects.append(button)

        button = NextPage(self)
        self.objects.append(button)
        button = LastPage(self)
        self.objects.append(button)
        self.show_page()

    def show_page(self):
        # Verify if the page was already instantiated
        if self.page in self.instantiated_pages:
            for i in range(len(self.objects)):
                if isinstance(self.objects[i], Card):
                    if self.page * 10 <= self.objects[i].id_card < 10 + self.page * 10:
                        self.objects[i].visible = True
            return

        y = 100
        x = 0
        for i in range(self.page * 10, 10 + self.page * 10, 1):
            if len(cards) > i:
                card = CardFactory.get_card_by_id(i)
                x += 150
                if i > 10 * self.page + 4:
                    card.current_pos = [x - 750, y + 200]
                else:
                    card.current_pos = [x, y]
                self.objects.append(card)

        self.instantiated_pages.append(self.page)
