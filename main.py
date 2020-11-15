import pygame
import globals
from scene_factory import SceneFactory

# Constants
MAIN_SCREEN_SIZE = (500, 500)
GAME_RHYTHM = 65

# Variables
clock = pygame.time.Clock()
scenes = [SceneFactory.instantiate_menu(), SceneFactory.instantiate_game()]


def update_game(main_window):
    # This render part could be separated in layers but fuck it
    # Starts with a black window and render the "layers"
    main_window.fill((0, 0, 0))

    scenes[globals.active_scene].input_reactions()
    scenes[globals.active_scene].render(main_window)

    # At the end of the renders just update the screen
    pygame.display.update()


def main_loop():
    global clock
    pygame.init()

    main_window = pygame.display.set_mode(MAIN_SCREEN_SIZE)
    pygame.display.set_caption("First Game")

    run = True
    while run:
        clock.tick(GAME_RHYTHM)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update game
        update_game(main_window)

    pygame.quit()


if __name__ == '__main__':
    main_loop()
