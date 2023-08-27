import random
import pygame
import consts
import game_field
import soldier
import screen

TELEPORT_IMAGE = 'teleport.png'
TELEPORT_NUM = 5
TELEPORT_LOCATIONS = []


def create_teleport():
    for i in range(TELEPORT_NUM):
        while True:
            col = random.randint(4, consts.GAME_GRID_COL - consts.MINE_WIDTH)
            row = random.randint(consts.SOLDIER_HEIGHT - 1, consts.GAME_GRID_ROW - consts.MINE_WIDTH)
            if game_field.game_grid[row][col:col + consts.MINE_WIDTH].count(consts.EMPTY) == consts.MINE_WIDTH:
                TELEPORT_LOCATIONS.append((col, row))
                break
        for j in range(consts.MINE_WIDTH):
            game_field.game_grid[row][col + j] = consts.TELEPORT


def draw_teleport():
    teleport = pygame.image.load(TELEPORT_IMAGE)
    sized_teleport = pygame.transform.scale(teleport, (
        consts.SQUARE_WIDTH * consts.MINE_WIDTH, consts.SQUARE_HEIGHT * consts.MINE_HEIGHT))
    for location in range(TELEPORT_NUM):
        screen.blit(sized_teleport,
                    (TELEPORT_LOCATIONS[location])
                     )


def put_teleport_in_grid():
    for location in TELEPORT_LOCATIONS:
        for j in range(consts.MINE_WIDTH):
            game_field.game_grid[location[1]][location[0] + j] = consts.TELEPORT


def is_on_teleport():
    for i in range(consts.SOLDIER_WIDTH):
        if game_field.game_grid[location[1] + consts.SOLDIER_HEIGHT - 1][location[0] + i] == consts.TELEPORT:
            return True
    return False

def To_Another_Teleport():
    if is_on_teleport()==True:
        ToAnotherTeleport = TELEPORT_LOCATIONS[random.randint(0,TELEPORT_NUM)]
        soldier.location = ToAnotherTeleport[0]+1,ToAnotherTeleport[1]
