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


def create_bushes_locations():
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0, consts.WINDOW_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT)
        consts.bush_locations.append((x, y))


def draw_bushes():
    bush = pygame.image.load(consts.BUSH_IMG)
    sized_bush = pygame.transform.scale(bush, (
        consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for bush in consts.bush_locations:
        screen.blit(sized_bush, bush)


def draw_soldier():
    soldier_img = pygame.image.load(consts.SOLDIER_IMG)
    sized_soldier = pygame.transform.scale(soldier_img, (
        40, 80))
    screen.blit(sized_soldier,
                ((consts.SQUARE_MARGIN + consts.SQUARE_WIDTH) * soldier.location[0] + consts.SQUARE_MARGIN,
                 (consts.SQUARE_MARGIN + consts.SQUARE_HEIGHT) * soldier.location[1] + consts.SQUARE_MARGIN))


def draw_flag():
    flagimg = pygame.image.load(consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(flagimg, (
        40, 80))
    screen.blit(sized_flag,
                ((consts.SQUARE_MARGIN + consts.SQUARE_WIDTH) * soldier.location[0] + consts.SQUARE_MARGIN,
                 (consts.SQUARE_MARGIN + consts.SQUARE_HEIGHT) * soldier.location[1] + consts.SQUARE_MARGIN))


def visualize_grid():
    mine = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine, (
        20, 20))
    screen.fill((0, 0, 0))
    for row in range(consts.GAME_GRID_ROW):
        for column in range(consts.GAME_GRID_COL):
            color = (255, 255, 255)
            pygame.draw.rect(screen, color,
                             [(consts.SQUARE_MARGIN + consts.SQUARE_WIDTH) * column + consts.SQUARE_MARGIN,
                              (consts.SQUARE_MARGIN + consts.SQUARE_HEIGHT) * row + consts.SQUARE_MARGIN,
                              consts.SQUARE_WIDTH, consts.SQUARE_HEIGHT])
            if game_field.game_grid[row][column] == consts.MINE:
                screen.blit(sized_mine, ((consts.SQUARE_MARGIN + consts.SQUARE_WIDTH) * column + consts.SQUARE_MARGIN,
                                         (consts.SQUARE_MARGIN + consts.SQUARE_HEIGHT) * row + consts.SQUARE_MARGIN))
    draw_soldier()
    pygame.display.flip()
