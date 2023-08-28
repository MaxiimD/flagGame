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
    consts.mine_locations = create_object((0, consts.GAME_GRID_COL - consts.MINE_WIDTH - 1),
                                          (consts.SOLDIER_HEIGHT - 1, consts.GAME_GRID_ROW - consts.SOLDIER_HEIGHT),
                                          consts.NUM_OF_MINES, consts.MINE_WIDTH, consts.MINE_HEIGHT, consts.MINE)


def create_flag():
    put_in_grid((consts.GAME_GRID_COL - consts.FLAG_WIDTH, consts.GAME_GRID_ROW - consts.FLAG_HEIGHT),
                consts.FLAG_WIDTH, consts.FLAG_HEIGHT, consts.EMPTY)


def create_teleport():
    consts.TELEPORT_LOCATIONS = create_object((0, consts.GAME_GRID_COL - consts.TELEPORT_WIDTH), (4, 20),
                                              consts.TELEPORT_NUM,
                                              consts.TELEPORT_WIDTH, consts.TELEPORT_HEIGHT, consts.TELEPORT)


def create_empty_matrix():
    global game_grid
    game_grid = [[consts.EMPTY for col in range(consts.GAME_GRID_COL)] for row in range(consts.GAME_GRID_ROW)]


def remove_mines():
    for location in consts.mine_locations:
        put_in_grid(location, consts.MINE_WIDTH, consts.MINE_HEIGHT, consts.EMPTY)


def remove_teleport():
    for location in consts.TELEPORT_LOCATIONS:
        put_in_grid(location, consts.TELEPORT_WIDTH, consts.TELEPORT_HEIGHT, consts.EMPTY)


def put_teleport_in_grid():
    for location in consts.TELEPORT_LOCATIONS:
        put_in_grid(location, consts.TELEPORT_WIDTH, consts.TELEPORT_HEIGHT, consts.TELEPORT)


def put_mines_in_grid():
    for location in consts.mine_locations:
        put_in_grid(location, consts.MINE_WIDTH, consts.MINE_HEIGHT, consts.MINE)


def load_from_db():
    remove_mines()
    remove_teleport()
    put_mines_in_grid()
    put_teleport_in_grid()


def put_in_grid(location: tuple, width=1, height=1, val=consts.EMPTY):
    """
    places values in grid by their starting location (top left)
    :param location:
    :param width:
    :param height:
    :param val:
    :return:
    """
    for row in range(height):
        for col in range(width):
            game_grid[location[1]][location[0] + col] = val


def create_object(col_limits: tuple, row_limits: tuple, num_of_object: int, object_width: int, object_height: int,
                  val: int):
    """
    :param col_limits:
    :param row_limits:
    :param num_of_object:
    :param object_width:
    :param object_height:
    :param val:
    :return:
    """
    soldier_location = soldier.soldier_body_locations()
    locations = []
    for i in range(num_of_object):
        while True:
            col = random.randint(col_limits[0], col_limits[1])
            row = random.randint(row_limits[0], row_limits[1])
            sub_matrix = [row[col:col + object_width] for row in game_grid[row:row + object_height]]
            if (sum(x.count(consts.EMPTY) for x in sub_matrix) ==
                    object_width * object_height
                    and not game_grid[row][col] in soldier_location):
                locations.append((col, row))
                break
        put_in_grid((col, row), object_width, object_height, val)
    return locations
