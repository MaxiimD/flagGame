import consts
import game_field

location = consts.SOLDIER_START_LOCATION


# def soldier_body_locations():
#     body_locations = []
#     for i in range(consts.SOLDIER_HEIGHT):
#         for j in range(consts.SOLDIER_WIDTH):
#             body_locations.append((location[0] + i, location[1] + j))
#     return body_locations
#
#
# def soldier_feet_locations():
#     feet_locations = []
#     for i in range(consts.SOLDIER_WIDTH):
#         feet_locations.append((location[0] + consts.SOLDIER_HEIGHT - 1, location[1] + i))
#     return feet_locations


def is_on_mine():
    for i in range(consts.SOLDIER_WIDTH):
        if game_field.game_grid[location[1] + consts.SOLDIER_HEIGHT - 1][location[0] + i] == consts.MINE:
            return True
    return False


def is_on_flag():
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            if game_field.game_grid[location[1] + i][location[0] + j] == consts.FLAG:
                return True
    return False
