import pygame
import sys
from pygame import *

# Define Constants
black = (0, 0, 0)
window_width = 600
window_height = 600
frames_per_second = 30

# initialize world
pygame.init()
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

# initialize loop
while True:

    # Event checker
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
    


    window.fill(black)

    pygame.display.update

    clock.tick(frames_per_second)