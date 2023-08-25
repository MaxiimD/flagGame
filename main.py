import consts
import pygame
import screen
import game_field
import soldier
import time
import database
import sys

state = {
    "is_window_open": True,
    "player_location": consts.SOLDIER_START_LOCATION,
    "is_player_moving": False,
    "is_in_grid_view": False,
    "state": consts.RUNNING_STATE
}


def main():
    pygame.init()
    game_field.create()
    screen.create_bushes_locations()
    database.init()
    while state["is_window_open"]:
        handle_user_events()
        if state["is_player_moving"]:
            move_soldier()
            state["is_player_moving"] = False
            if soldier.is_on_mine():
                state["state"] = consts.LOSE_STATE
            elif soldier.is_on_flag():
                state["state"] = consts.WIN_STATE
        elif state["is_in_grid_view"]:
            grid_view()
            state["is_in_grid_view"] = False
        screen.draw_game(state)


def handle_user_events():
    global t
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            time.sleep(3)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state["is_in_grid_view"] = True
            if event.key in consts.NUMBER_KEYS:
                t = time.time()
            if event.key in consts.MOVEMENT_KEYS:
                state["is_player_moving"] = True
        if event.type == pygame.KEYUP:
            if event.key in consts.NUMBER_KEYS:
                time_elapsed = time.time() - t
                print(time_elapsed)


# def print_mat(mat: list):
#     for row in range(len(mat)):
#         for col in range(len(mat[row])):
#             print(mat[row][col], end=' ')
#         print()


def grid_view():
    screen.visualize_grid()
    time.sleep(consts.GRID_VIEW_TIME)


def move_soldier():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if not soldier.location[0] - consts.SOLDIER_STEP < 0:
            soldier.location[0] -= consts.SOLDIER_STEP
    elif keys[pygame.K_RIGHT]:
        if not soldier.location[0] + consts.SOLDIER_STEP > consts.GAME_GRID_COL - consts.SOLDIER_WIDTH:
            soldier.location[0] += consts.SOLDIER_STEP
    elif keys[pygame.K_UP]:
        if not soldier.location[1] - consts.SOLDIER_STEP < 0:
            soldier.location[1] -= consts.SOLDIER_STEP
    elif keys[pygame.K_DOWN]:
        if not soldier.location[1] + consts.SOLDIER_STEP > consts.GAME_GRID_ROW - consts.SOLDIER_HEIGHT:
            soldier.location[1] += consts.SOLDIER_STEP


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
