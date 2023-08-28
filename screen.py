import random
from typing import Union, Any

import consts
import pygame
import soldier
import guard

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_welcome_msg()
    draw_bushes()
    draw_soldier(consts.SOLDIER_IMG)
    draw_flag()
    draw_teleport()
    draw_guard(consts.GUARD_IMG)
    if game_state["state"] == consts.LOSE_STATE:
        visualize_grid()
        draw_lose_message()
    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()
    pygame.display.flip()


def draw_object(img: str, width: int, height: int, location: tuple[int], direction: str = consts.RIGHT):
    """
    This func draws an object on screen
    :param direction:
    :param img:
    :param width:
    :param height:
    :param location:
    """
    img = pygame.image.load(img)
    sized_img = pygame.transform.scale(img, (
        consts.SQUARE_WIDTH * width, consts.SQUARE_HEIGHT * height))
    if direction != consts.RIGHT:
        sized_img = pygame.transform.flip(sized_img, True, False)
    screen.blit(sized_img,
                (location[0], location[1]))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_welcome_msg():
    draw_message(consts.WELCOME_MSG, consts.WELCOME_FONT_SIZE,
                 consts.WELCOME_COLOR, consts.WELCOME_LOCATION)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def create_bushes_locations():
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0, consts.WINDOW_WIDTH - consts.BUSH_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT - consts.BUSH_HEIGHT)
        consts.bush_locations.append((x, y))


def draw_bushes():
    for location in consts.bush_locations:
        draw_object(consts.BUSH_IMG, consts.BUSH_WIDTH, consts.BUSH_HEIGHT, location)


def draw_soldier(img):
    draw_object(img, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT, calc_pixels(soldier.location))


def draw_guard(img):
    draw_object(img, consts.GUARD_WIDTH, consts.GUARD_HEIGHT, calc_pixels(guard.location),guard.direction)


def draw_flag():
    draw_object(consts.FLAG_IMG, consts.FLAG_WIDTH, consts.FLAG_HEIGHT, consts.FLAG_LOCATION)


def draw_mines():
    for location in consts.mine_locations:
        draw_object(consts.MINE_IMG, consts.MINE_WIDTH, consts.MINE_HEIGHT, calc_pixels(location))


def draw_teleport():
    for location in consts.TELEPORT_LOCATIONS:
        draw_object(consts.TELEPORT_IMAGE, consts.TELEPORT_WIDTH, consts.TELEPORT_HEIGHT, calc_pixels(location))


def visualize_grid():
    screen.fill(consts.BACKGROUND_XRAY)
    for row in range(consts.GAME_GRID_ROW):
        for column in range(consts.GAME_GRID_COL):
            pygame.draw.rect(screen, consts.SQUARE_COLOR,
                             [consts.SQUARE_WIDTH * column,
                              consts.SQUARE_HEIGHT * row,
                              consts.SQUARE_WIDTH, consts.SQUARE_HEIGHT], consts.SQUARE_BORDER)
    draw_mines()
    draw_soldier(consts.SOLDIER_IMG_NIGHT)
    draw_guard(consts.GUARD_IMG_NIGHT)
    pygame.display.flip()


def calc_pixels(grid_location: Union[tuple[int], list[int]]) -> tuple:
    x = grid_location[0] * consts.SQUARE_WIDTH
    y = grid_location[1] * consts.SQUARE_WIDTH
    return x, y
