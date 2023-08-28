import random
import consts
import game_field
import soldier


def is_on_teleport():
    feet_locations = soldier.soldier_feet_locations()
    for f_location in feet_locations:
        if game_field.game_grid[f_location[0]][f_location[1]] == consts.TELEPORT:
            return True
    return False


def teleport():
    tp = random.choice(consts.TELEPORT_LOCATIONS)
    soldier.location = [tp[0], tp[1] - consts.SOLDIER_HEIGHT]
