import consts
import pygame

import guard
import screen
import game_field
import soldier
import database

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
    clock = pygame.time.Clock()
    # print_mat(game_field.game_grid)
    pygame.time.set_timer(pygame.USEREVENT, 100)
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
            pygame.time.set_timer(pygame.USEREVENT, 0)
            grid_view()
            pygame.time.set_timer(pygame.USEREVENT, 100)
            state["is_in_grid_view"] = False
        if guard.is_colliding_with_soldier():
            state["state"] = consts.LOSE_STATE
        screen.draw_game(state)
        clock.tick(consts.FPS)


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            pygame.time.delay(consts.WIN_LOSE_MSG_TIME * 1000)
            state["is_window_open"] = False
        if event.type == pygame.USEREVENT:
            guard.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state["is_in_grid_view"] = True
            if event.key in consts.NUMBER_KEYS_TIME_DICT:
                consts.NUMBER_KEYS_TIME_DICT[event.key] = pygame.time.get_ticks()
            if event.key in consts.MOVEMENT_KEYS:
                state["is_player_moving"] = True
        if event.type == pygame.KEYUP:
            if event.key in consts.NUMBER_KEYS_TIME_DICT:
                consts.NUMBER_KEYS_TIME_DICT[event.key] = pygame.time.get_ticks() - consts.NUMBER_KEYS_TIME_DICT[
                    event.key]
                if consts.NUMBER_KEYS_TIME_DICT[event.key] > consts.SAVE_TIME * 1000:
                    database.save(event.key)
                else:
                    load_game(event.key)


def print_mat(mat: list):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            print(mat[row][col], end=' ')
        print()


def grid_view():
    screen.visualize_grid()
    pygame.time.delay(consts.GRID_VIEW_TIME * 1000)


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


def load_game(key):
    database.load(key)
    game_field.load_from_db()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
