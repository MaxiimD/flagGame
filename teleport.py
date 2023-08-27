import random
import consts
import game_field
import soldier


def is_on_teleport():
    for i in range(consts.SOLDIER_WIDTH):
        if game_field.game_grid[soldier.location[1] +
                                consts.SOLDIER_HEIGHT - 1][soldier.location[0] + i] == consts.TELEPORT:
            return True
    return False


def teleport():
    tp = consts.TELEPORT_LOCATIONS[random.randint(0, consts.TELEPORT_NUM-1)]
    soldier.location = [tp[1] + consts.SOLDIER_HEIGHT, tp[0]]
