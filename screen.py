import random
import consts
import pygame
import soldier
import guard

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_bushes()
    draw_soldier(consts.SOLDIER_IMG)
    draw_flag()
    draw_teleport()
    draw_guard(guard.GUARD_IMG)
    if game_state["state"] == consts.LOSE_STATE:
        visualize_grid()
        draw_lose_message()
    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()
    pygame.display.flip()


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def create_bushes_locations():
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0, consts.WINDOW_WIDTH - consts.BUSH_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT - consts.BUSH_HEIGHT)
        consts.bush_locations.append((x, y))


def draw_bushes():
    bush = pygame.image.load(consts.BUSH_IMG)
    sized_bush = pygame.transform.scale(bush, (
        consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for bush in consts.bush_locations:
        screen.blit(sized_bush, bush)


def draw_soldier(img):
    soldier_img = pygame.image.load(img)
    sized_soldier = pygame.transform.scale(soldier_img, (
        consts.SQUARE_WIDTH * consts.SOLDIER_WIDTH, consts.SQUARE_HEIGHT * consts.SOLDIER_HEIGHT))
    screen.blit(sized_soldier,
                (consts.SQUARE_WIDTH * soldier.location[0],
                 consts.SQUARE_HEIGHT * soldier.location[1]))


def draw_guard(img):
    guard_img = pygame.image.load(img)
    sized_guard = pygame.transform.scale(guard_img, (
        consts.SQUARE_WIDTH * consts.GUARD_WIDTH, consts.SQUARE_HEIGHT * consts.GUARD_HEIGHT))
    if guard.direction == 'L':
        sized_guard = pygame.transform.flip(sized_guard, True, False)
    screen.blit(sized_guard,
                (consts.SQUARE_WIDTH * guard.location[0],
                 consts.SQUARE_HEIGHT * guard.location[1]))


def draw_flag():
    flag_img = pygame.image.load(consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(flag_img, (
        consts.SQUARE_WIDTH * consts.FLAG_WIDTH, consts.SQUARE_HEIGHT * consts.FLAG_HEIGHT))
    screen.blit(sized_flag,
                ((consts.WINDOW_WIDTH - sized_flag.get_width()), (consts.WINDOW_HEIGHT - sized_flag.get_height())))


def draw_mines():
    mine = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine, (
        consts.SQUARE_WIDTH * consts.MINE_WIDTH, consts.SQUARE_HEIGHT * consts.MINE_HEIGHT))
    for location in consts.mine_locations:
        screen.blit(sized_mine,
                    (consts.SQUARE_WIDTH * location[0],
                     consts.SQUARE_HEIGHT * location[1]))


def visualize_grid():
    screen.fill(consts.BACKGROUND_XRAY)
    for row in range(consts.GAME_GRID_ROW):
        for column in range(consts.GAME_GRID_COL):
            pygame.draw.rect(screen, consts.SQUARE_COLOR,
                             [consts.SQUARE_WIDTH * column,
                              consts.SQUARE_HEIGHT * row,
                              consts.SQUARE_WIDTH, consts.SQUARE_HEIGHT], consts.SQUARE_BORDER)
    draw_mines()
    draw_soldier(consts.SOLDIER_IMG_XRAY)
    pygame.display.flip()


def draw_teleport():
    teleport = pygame.image.load(consts.TELEPORT_IMAGE)
    sized_teleport = pygame.transform.scale(teleport, (
        consts.SQUARE_WIDTH * consts.MINE_WIDTH, consts.SQUARE_HEIGHT * consts.MINE_HEIGHT))
    for location in consts.TELEPORT_LOCATIONS:
        screen.blit(sized_teleport,
                    (consts.SQUARE_WIDTH * location[0],
                     consts.SQUARE_HEIGHT * location[1]))
