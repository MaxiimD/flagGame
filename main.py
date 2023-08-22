import consts
import pygame
import screen

state = {
    "is_window_open": True,
    "player_location": [0,0],
    "state": consts.RUNNING_STATE
}


def main():
    pygame.init()
    while state["is_window_open"]:
        handle_user_events()


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
