import consts
import pygame
import screen

pygame.init()
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.draw_game()
pygame.quit()