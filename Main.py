import pygame
import sys
import math
from constants import *
from Tank import tank
from Shot import shot
import random

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    clock = pygame.time.Clock()
    player = tank(window)
    dt = 0
    shots = []
    

    # initialize loop
    while True:

        # Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update(dt)
        if player.update(dt):
            shots.append(shot(window, player.cannon_tip_x, player.cannon_tip_y, math.radians(player.angle), black))
        [rep.update() for rep in shots]

        window.fill(white)

        player.draw()
        [rep.draw() for rep in shots]

        pygame.display.update()
        dt = clock.tick(frames_per_second) / 1000


if __name__ == "__main__":
    main()