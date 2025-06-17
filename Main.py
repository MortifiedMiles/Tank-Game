import pygame
import sys
from constants import *
from Tank import tank

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    clock = pygame.time.Clock()
    player = tank(window)
    dt = 0
    

    # initialize loop
    while True:

        # Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update(dt)
        for bullet in player.bullets:
            bullet.update()

        window.fill(white)

        player.draw()
        for bullet in player.bullets:
            bullet.draw()

        pygame.display.update()
        dt = clock.tick(frames_per_second) / 1000


if __name__ == "__main__":
    main()