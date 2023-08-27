import consts
import soldier

GUARD_IMG = 'guard.png'
location = consts.GUARD_STARTING_LOCATION
direction = consts.RIGHT


def move():
    global location
    is_colliding_with_wall()
    if direction == consts.RIGHT:
        location[0] += 1
    else:
        location[0] -= 1


def is_colliding_with_soldier():
    guard_location = guard_body_locations()
    soldier_location = soldier.soldier_body_locations()
    for b_location in guard_location:
        if b_location in soldier_location:
            return True
    return False


def is_colliding_with_wall():
    global direction
    if location[0] + consts.SOLDIER_STEP > consts.GAME_GRID_COL - consts.GUARD_WIDTH:
        direction = consts.LEFT
    elif location[0] - consts.SOLDIER_STEP < 0:
        direction = consts.RIGHT


def guard_body_locations():
    body_locations = []
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            body_locations.append((location[1] + i, location[0] + j))
    return body_locations
