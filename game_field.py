import consts

game_grid = []


def create():
    global game_grid
    game_grid = [[0 for x in range(consts.GAME_GRID_COL)] for y in range(consts.GAME_GRID_ROW)]


def create_mine():
    for i in range(consts.NUM_OF_MINES):
        pass

def create_flag():
    for i in range(game_grid):
        pass
