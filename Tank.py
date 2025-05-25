import pygame
from pygame import *

class tank():
    def __init__(self, window, angle = 10, x_start = 50, y_start = 400, imagefile = "Images/Tank1-1.png.png", 
                 scalefactor = 1, x_speed = 4, key_inputs = {'left': K_LEFT, 'right': K_RIGHT, 'aim_up': K_UP, 'aim_down': K_DOWN, 'shoot': K_SPACE}):
        self.image = pygame.image.load(imagefile)
        self.image = pygame.transform.scale_by(self.image, scalefactor)
        self._rect = self.image.get_rect()

        self._x = x_start
        self._y = y_start
        self.window = window
        self.scalefactor = scalefactor
        self.x_speed = x_speed
        self.key_inputs = key_inputs
        self.angle = angle

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

    def draw(self):
        self.window.blit(self.image, self.pos)
    
    @property
    def x_speed(self):
        return self._x_speed
    
    @x_speed.setter
    def x_speed(self, new_x_speed):
        self._x_speed = new_x_speed
    
    def manual_controls(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.key_inputs['left']]:
            self.x -= self.x_speed
        if keys_pressed[self.key_inputs['right']]:
            self.x += self.x_speed
        if keys_pressed[self.key_inputs['shoot']]:
            return True # figure out how to create a shot, and set a limit for how often one can shoot
        if self.angle < 90 and self.angle > 0: 
            if keys_pressed[self.key_inputs['aim_up']]:
                self.angle += 2
            if keys_pressed[self.key_inputs['aim_down']]:
                self.angle -= 2
            
        


