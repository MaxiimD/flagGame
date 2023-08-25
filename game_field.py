import consts
import random
import soldier

game_grid = []


def create():
    create_empty_matrix()
    create_player()
    create_flag()
    create_mines()


def create_mines():
    for i in range(consts.NUM_OF_MINES):
        while True:
            x = random.randint(0, consts.GAME_GRID_COL - consts.MINE_WIDTH)
            y = random.randint(consts.SOLDIER_HEIGHT - 1, consts.GAME_GRID_ROW - consts.MINE_WIDTH)
            if game_grid[y][x:x + consts.MINE_WIDTH].count(consts.EMPTY) == consts.MINE_WIDTH:
                consts.mine_locations.append((x, y))
                break
        for j in range(consts.MINE_WIDTH):
            game_grid[y][x + j] = consts.MINE


def create_flag():
    for i in range(consts.FLAG_HEIGHT):
        for j in range(consts.FLAG_WIDTH):
            game_grid[consts.GAME_GRID_ROW - consts.FLAG_HEIGHT + i][
                consts.GAME_GRID_COL - consts.FLAG_WIDTH + j] = consts.FLAG


def create_player():
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            game_grid[i][j] = consts.SOLIDER


def create_empty_matrix():
    global game_grid
    game_grid = [[consts.EMPTY for x in range(consts.GAME_GRID_COL)] for y in range(consts.GAME_GRID_ROW)]
