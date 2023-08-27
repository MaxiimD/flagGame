import consts
import random
import soldier

game_grid = []


def create():
    create_empty_matrix()
    create_flag()
    create_mines()
    create_teleport()


def create_mines():
    soldier_location = soldier.soldier_body_locations()
    for i in range(consts.NUM_OF_MINES):
        while True:
            col = random.randint(0, consts.GAME_GRID_COL - consts.MINE_WIDTH)
            row = random.randint(consts.SOLDIER_HEIGHT - 1, consts.GAME_GRID_ROW - 1)
            if (game_grid[row][col:col + consts.MINE_WIDTH].count(consts.EMPTY) == consts.MINE_WIDTH
                    and not game_grid[row][col] in soldier_location):
                consts.mine_locations.append((col, row))
                break
        for j in range(consts.MINE_WIDTH):
            game_grid[row][col + j] = consts.MINE


def put_mines_in_grid():
    for location in consts.mine_locations:
        for j in range(consts.MINE_WIDTH):
            game_grid[location[1]][location[0] + j] = consts.MINE


def create_flag():
    for i in range(consts.FLAG_HEIGHT):
        for j in range(consts.FLAG_WIDTH):
            game_grid[consts.GAME_GRID_ROW - consts.FLAG_HEIGHT + i][
                consts.GAME_GRID_COL - consts.FLAG_WIDTH + j] = consts.FLAG


def create_empty_matrix():
    global game_grid
    game_grid = [[consts.EMPTY for col in range(consts.GAME_GRID_COL)] for row in range(consts.GAME_GRID_ROW)]


def remove_mines():
    global game_grid
    for row in range(len(game_grid)):
        for col in range(len(game_grid[row])):
            if game_grid[row][col] == consts.MINE:
                game_grid[row][col] = consts.EMPTY


def load_from_db():
    remove_mines()
    put_mines_in_grid()


def create_teleport():
    soldier_location = soldier.soldier_body_locations()
    for i in range(consts.TELEPORT_NUM):
        while True:
            col = random.randint(4, consts.GAME_GRID_COL - consts.MINE_WIDTH)
            row = random.randint(consts.SOLDIER_HEIGHT - 1, consts.GAME_GRID_ROW - consts.MINE_WIDTH)
            if (game_grid[row][col:col + consts.MINE_WIDTH].count(consts.EMPTY) == consts.MINE_WIDTH
                    and not (row, col) in soldier_location):
                consts.TELEPORT_LOCATIONS.append((col, row))
                break
        for j in range(consts.MINE_WIDTH):
            game_grid[row][col + j] = consts.TELEPORT


def put_teleport_in_grid():
    for location in consts.TELEPORT_LOCATIONS:
        for j in range(consts.MINE_WIDTH):
            game_grid[location[1]][location[0] + j] = consts.TELEPORT
