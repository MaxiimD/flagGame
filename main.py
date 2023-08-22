import consts
import pygame
import screen
import game_field

state = {
    "is_window_open": True,
    "player_location": consts.SOLDIER_START_LOCATION,
    "state": consts.RUNNING_STATE
}


def main():
    # pygame.init()
    game_field.create()
    print_mat(game_field.game_grid)
    # while state["is_window_open"]:
    #     handle_user_events()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_RETURN:
                pass


def print_mat(mat: list):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            print(mat[row][col], end=' ')
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
