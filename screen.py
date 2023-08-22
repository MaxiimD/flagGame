import random
import consts
import pygame
import soldier

import game_field

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_bushes()
    draw_soldier()
    # Flip the display
    pygame.display.flip()


def updated_game():
    draw_soldier()
    pygame.display.update()


def draw_bushes():
    bush = pygame.image.load(consts.BUSH_IMG)
    sized_bush = pygame.transform.scale(bush, (
        consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0, consts.WINDOW_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT)
        screen.blit(sized_bush, (x, y))


def draw_soldier():
    soldierimg = pygame.image.load(consts.SOLDIER_IMG)
    sized_soldier = pygame.transform.scale(soldierimg, (
        40, 80))
    screen.blit(sized_soldier,
                ((MARGIN + WIDTH) * soldier.location[0] + MARGIN, (MARGIN + HEIGHT) * soldier.location[1] + MARGIN))


def draw_flag():
    flagimg = pygame.image.load(consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(flagimg, (
        40, 80))
    screen.blit(sized_flag,
                ((MARGIN + WIDTH) * soldier.location[0] + MARGIN, (MARGIN + HEIGHT) * soldier.location[1] + MARGIN))


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 1


def visualize_grid():
    mine = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine, (
        20, 20))
    screen.fill((0, 0, 0))
    for row in range(consts.GAME_GRID_ROW):
        for column in range(consts.GAME_GRID_COL):
            color = (255, 255, 255)
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            if game_field.game_grid[row][column] == consts.MINE:
                screen.blit(sized_mine, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
    draw_soldier()
    pygame.display.flip()
