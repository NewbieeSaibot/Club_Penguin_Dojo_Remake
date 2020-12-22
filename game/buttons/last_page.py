from engine.button import Button
from engine.card import Card


class LastPage(Button):
    def __init__(self, scene):
        super().__init__(self.next_page, x=730, y=480, width=50, height=50, cool_down=5)
        self.image_path = "./game/data/images/buttons/last_page.png"
        self.scene = scene

    def next_page(self):
        # set all current cards to invisible mode
        for i in range(0, len(self.scene.objects), 1):
            if isinstance(self.scene.objects[i], Card):
                self.scene.objects[i].visible = False

        # Set to next page
        self.scene.page = (self.scene.page - 1) % self.scene.total_pages

        # Show the new page
        self.scene.show_page()
