import pygame
import sys
from pygame import *
from Tank import tank
from Shot import shot

# Define Constants
black = (0, 0, 0)
window_width = 600
window_height = 600
frames_per_second = 30

# initialize world
pygame.init()
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
player = tank(window)
dt = 0
shots = shot(window, 600, 0, dt, 10, 45)

# initialize loop
while True:

    # Event checker
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player.manual_controls()
    shots.update()

    window.fill(black)

    player.draw()
    shots.draw()

    pygame.display.update()


    clock.tick(frames_per_second)
    dt += 0.5