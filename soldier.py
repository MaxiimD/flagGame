import consts
import game_field

location = consts.SOLDIER_START_LOCATION


def soldier_body_locations():
    body_locations = []
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            body_locations.append((location[1] + i, location[0] + j))
    return body_locations


def soldier_feet_locations():
    feet_locations = []
    for i in range(consts.SOLDIER_WIDTH):
        feet_locations.append((location[1] + consts.SOLDIER_HEIGHT - 1, location[0] + i))
    return feet_locations


def is_on_mine():
    feet_locations = soldier_feet_locations()
    for f_location in feet_locations:
        if game_field.game_grid[f_location[0]][f_location[1]] == consts.MINE:
            return True
    return False


def is_on_flag():
    body_locations = soldier_body_locations()
    for b_location in body_locations:
        if game_field.game_grid[b_location[0]][b_location[1]] == consts.FLAG:
            return True
    return False
