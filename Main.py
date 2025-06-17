import pygame
import sys
from constants import *
from Tank import tank

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    clock = pygame.time.Clock()
    player1 = tank(window)
    player2 = tank(window, 950, 400, 100, {'left': pygame.K_a, 'right': pygame.K_d, 'aim_up': pygame.K_w, 'aim_down': pygame.K_s, 'shoot': pygame.K_TAB})
    players = [player1, player2]
    dt = 0
    

    # initialize loop
    while True:

        # Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for player in players:
            player.update(dt)
            for bullet in player.bullets:
                bullet.update()

        window.fill(white)
        for player in players:
            player.draw()
            for bullet in player.bullets:
                bullet.draw()

        pygame.display.update()
        dt = clock.tick(frames_per_second) / 100


if __name__ == "__main__":
    main()