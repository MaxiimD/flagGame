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
        for i in range(consts.MINE_WIDTH):
            game_grid[location[1]][location[0] + i] = consts.MINE


def create_flag():
    for row in range(consts.FLAG_HEIGHT):
        for col in range(consts.FLAG_WIDTH):
            game_grid[consts.GAME_GRID_ROW - consts.FLAG_HEIGHT + row][
                consts.GAME_GRID_COL - consts.FLAG_WIDTH + col] = consts.FLAG


def create_empty_matrix():
    global game_grid
    game_grid = [[consts.EMPTY for col in range(consts.GAME_GRID_COL)] for row in range(consts.GAME_GRID_ROW)]


def remove_mines():
    global game_grid
    for location in consts.mine_locations:
        for i in range(consts.MINE_WIDTH):
            game_grid[location[1]][location[0] + i] = consts.EMPTY


def create_teleport():
    soldier_location = soldier.soldier_body_locations()
    for i in range(consts.TELEPORT_NUM):
        while True:
            col = random.randint(0, consts.GAME_GRID_COL - consts.TELEPORT_WIDTH)
            row = random.randint(4, 20)
            if (game_grid[row][col:col + consts.TELEPORT_WIDTH].count(consts.EMPTY) == consts.MINE_WIDTH
                    and not (row, col) in soldier_location):
                consts.TELEPORT_LOCATIONS.append((col, row))
                break
        for j in range(consts.TELEPORT_WIDTH):
            game_grid[row][col + j] = consts.TELEPORT


def put_teleport_in_grid():
    for location in consts.TELEPORT_LOCATIONS:
        for i in range(consts.TELEPORT_WIDTH):
            game_grid[location[1]][location[0] + i] = consts.TELEPORT


def remove_teleport():
    global game_grid
    for location in consts.TELEPORT_LOCATIONS:
        put_in_grid(location, consts.EMPTY, consts.TELEPORT_WIDTH, consts.TELEPORT_HEIGHT)
        # for i in range(consts.TELEPORT_WIDTH):
        #     game_grid[location[1]][location[0] + i] = consts.EMPTY


def load_from_db():
    remove_mines()
    remove_teleport()
    put_mines_in_grid()
    put_teleport_in_grid()


def put_in_grid(location, val, cols=1, rows=1):
    for row in range(rows):
        for col in range(cols):
            game_grid[location[1] + row][location[0] - consts.FLAG_WIDTH + col] = val


def create_object(col_limits: tuple, row_limits, num_of_object, object_width, object_height):
    soldier_location = soldier.soldier_body_locations()
    for i in range(consts.NUM_OF_MINES):
        while True:
            col = random.randint(col_limits[0], col_limits[1])
            row = random.randint(row_limits[0], row_limits[1])
            if (game_grid[row:col + object_height][col:col + object_width].count(consts.EMPTY) ==
                    object_width + object_height
                    and not game_grid[row][col] in soldier_location):
                consts.mine_locations.append((col, row))
                break
        for j in range(consts.MINE_WIDTH):
            game_grid[row][col + j] = consts.MINE
