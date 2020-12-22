import pygame
from game import globals
from game.scenes import game, menu, shop

# Variables
clock = pygame.time.Clock()
scenes = [menu.Menu(), game.Game(), shop.Shop()]


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
    pygame.mixer.music.load("./game/data/sounds/backgrounds/theme.mp3")
    pygame.mixer.music.play(-1)

    main_window = pygame.display.set_mode(globals.MAIN_SCREEN_SIZE)
    pygame.display.set_caption(globals.GAME_NAME)

    run = True
    while run:
        clock.tick(globals.GAME_RHYTHM)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update game
        update_game(main_window)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
