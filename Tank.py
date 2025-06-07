import pygame
from constants import *
from Shot import shot

class tank():
    def __init__(self, window, x_start = 50, y_start = 400, key_inputs = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'aim_up': pygame.K_UP, 'aim_down': pygame.K_DOWN, 'shoot': pygame.K_SPACE}):
        self._x = x_start
        self._y = y_start
        self.window = window
        self.key_inputs = key_inputs
        self._angle = 10
        self.shoot_timer = 0
        self.cannon = pygame.Surface((cannon_width, cannon_height), pygame.SRCALPHA)
        pygame.draw.rect(self.cannon, cannon_color, self.cannon.get_rect())

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

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, new_angle):
        self._angle = new_angle

    def draw(self):
        ## Draw the tank body
        pygame.draw.rect(self.window, player_color, (self._x, self._y, player_width, player_height), 1)

        ## Draw the cannon
        # Set the position of the cannon
        cannon_x = self._x + player_width / 2
        cannon_y = self._y + player_height / 2
        # Establish pivots
        pivot_world = pygame.Vector2(cannon_x, cannon_y)
        pivot_offset = pygame.Vector2(0, cannon_height / 2)
        # Rotate the cannon
        rotated_cannon = pygame.transform.rotate(self.cannon, self.angle)
        rotated_offset = pivot_offset.rotate(-self.angle)
        new_topleft = pivot_world - rotated_offset
        # Draw rotated cannon
        self.window.blit(rotated_cannon, new_topleft)
        

    
    @property
    def x_speed(self):
        return self._x_speed
    
    @x_speed.setter
    def x_speed(self, new_x_speed):
        self._x_speed = new_x_speed
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.key_inputs['left']]:
            self.x -= player_speed * dt
        if keys_pressed[self.key_inputs['right']]:
            self.x += player_speed * dt
        if keys_pressed[self.key_inputs['shoot']]:
            return True # figure out how to create a shot, and set a limit for how often one can shoot
        if keys_pressed[self.key_inputs['aim_up']]:
            self.angle += aim_speed * dt
        if keys_pressed[self.key_inputs['aim_down']]:
            self.angle -= aim_speed * dt