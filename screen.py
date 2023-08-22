import random
import consts
import pygame
import turtle

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    # Flip the display
    pygame.display.flip()


def draw_Night():
    screen.fill(consts.BACKGROUND_NIGHTCOLOR)
    # Flip the displayy
    pygame.display.flip()


def create_bushes(BUSH_IMG):
    bush = pygame.image.load(BUSH_IMG)
    sized_bush = pygame.transform.scale(bush, (
        consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    bush_box = pygame.Surface(
        (consts.BUSH_HEIGHT, consts.BUSH_HEIGHT), )
    bush_box.fill(consts.BACKGROUND_COLOR)

    return sized_bush


def draw_bushes(bush):
    for i in range(consts.NUM_OF_BUSHES):
        rotated_bush_rect = bush.get_rect(
            rnd=(random.randint(0, 1000), random.randint(0, 500)))
        screen.blit(bush, rotated_bush_rect)


def create_mine(MINE_IMG):
    mine = pygame.image.load(MINE_IMG)
    sized_mine = pygame.transform.scale(mine, (
        consts.MINE_WIDTH, consts.MINE_HEIGHT))
    mine_box = pygame.Surface(
        (consts.MINE_WIDTH, consts.MINE_HEIGHT), )
    mine_box.fill(consts.BACKGROUND_COLOR)

    return sized_mine


def draw_mine(mine):
    for i in range(consts.NUM_OF_MINES):
        rotated_bush_rect = mine.get_rect(
            rnd=(random.randint(0, 1000), random.randint(0, 500)))
        screen.blit(mine, rotated_bush_rect)


def create_soldier(SOLDIER_IMG):
    soldier = pygame.image.load(SOLDIER_IMG)
    sized_soldier = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    soldier_box = pygame.Surface(
        (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT), )
    soldier_box.fill(consts.BACKGROUND_COLOR)
    soldier_box.blit(sized_soldier, consts.SOLDIER_START_LOCATION)

    return sized_soldier


def draw_soldier(soldier):
    rotated_soldier_rect = soldier.get_rect(
        topleft=(consts.SOLDIER_BOTTOM_Y, consts.SOLDIER_BOTTOM_X))
    screen.blit(soldier, rotated_soldier_rect)
