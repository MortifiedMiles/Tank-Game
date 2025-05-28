import pygame
import sys
from pygame import *
import math as maths
from Tank import tank
from Shot import shot
import random

# Define Constants
black = (0, 0, 0)
white = (200, 200, 200)
window_width = 1000
window_height = 600
frames_per_second = 30

# initialize world
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
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player.manual_controls()
    if player.manual_controls():
        shots.append(shot(window, player.center_x, player.center_y, dt, random.randrange(10,25), maths.radians(player.angle), black, -9.8, 5))
    [rep.update(dt) for rep in shots]

    window.fill(white)

    player.draw()
    [rep.draw() for rep in shots]

    pygame.display.update()


    clock.tick(frames_per_second)
    dt += 0.25