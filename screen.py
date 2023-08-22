import consts
import pygame

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    # Flip the display
    pygame.display.flip()

def draw_bushes():
    for i in range(consts.NUM_OF_BUSHES):
