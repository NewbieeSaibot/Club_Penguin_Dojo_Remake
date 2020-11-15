from button import Button
import globals


class ButtonFactory:

    def __init__(self):
        pass

    @staticmethod
    def menu_button():
        def func():
            globals.active_scene = 1

        return Button(func, x=200)
