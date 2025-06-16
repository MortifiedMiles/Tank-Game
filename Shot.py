import pygame
import math
from constants import *


class shot():
    def __init__(self, window, x_start, y_start, angle, color = (155, 155, 155)):
        self.window = window
        self._x = x_start
        self._y = y_start
        self._color = color
        self.angle = angle
        self.creation_time = pygame.time.get_ticks()/1000
    
    @property
    def pos(self):
        return (self._x, self._y)
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        self._y = new_y
    
    def update(self):
        self.time_difference = pygame.time.get_ticks()/1000 - self.creation_time
        if shot_speed > 0:
            x_displacement = shot_speed * math.cos(self.angle) * self.time_difference
            y_displacement = shot_speed * math.sin(self.angle) * self.time_difference + (gravity * self.time_difference * self.time_difference)/2

            self.x += x_displacement
            self.y -= y_displacement

            if self.y >= 600 - shot_radius:
                del self


    def draw(self):
        pygame.draw.circle(self.window, self._color, self.pos, shot_radius)