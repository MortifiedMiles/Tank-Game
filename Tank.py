import pygame
import math
from constants import *
from Shot import shot

class tank():
    def __init__(self, window, player_color = player1_color, x_start = 144, y_start = 480, angle_start = 80, key_inputs = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'aim_up': pygame.K_UP, 'aim_down': pygame.K_DOWN, 'shoot': pygame.K_SPACE}):
        self._x = x_start
        self._y = y_start
        self.window = window
        self.key_inputs = key_inputs
        self._angle = angle_start
        self.shoot_timer = 0
        self.tank_body = pygame.Surface((player_width, player_height), pygame.SRCALPHA)
        self.tank_body.fill(player_color)
        self.cannon = pygame.Surface((cannon_width, cannon_height), pygame.SRCALPHA)
        self.cannon.fill(black)
        self._bullets = []
    
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

    @property
    def cannon_x(self):
        return self._x + player_width / 2

    @property
    def cannon_y(self):
        return self._y + player_height / 2
    
    @property
    def cannon_tip_x(self):
        return self.cannon_x + math.cos(math.radians(-self.angle)) * cannon_width

    @property
    def cannon_tip_y(self):
        return self.cannon_y + math.sin(math.radians(-self.angle)) * cannon_width
    
    @property
    def bullets(self):
        return self._bullets
    
    @bullets.setter
    def bullets(self, new_bullet):
        self._bullets.append(new_bullet)

    def draw(self):
        ## Draw the tank body
        rotation_angle = math.degrees(math.atan((ground_points[round(self.x)][1] - 
                                   ground_points[round(self.x + player_width)][1]) / 
                                   player_width))
        self.y = ground_points[round(self.x)][1] - player_height
        rotated_tank = pygame.transform.rotate(self.tank_body, rotation_angle)
        self.window.blit(rotated_tank, (self.x, self.y))

        ## Draw the cannon
        # Establish pivots
        pivot_point = pygame.Vector2(self.cannon_x, self.cannon_y)
        pivot_offset = pygame.Vector2(cannon_width / 2, 0)
        # Rotate the cannon
        rotated_cannon = pygame.transform.rotate(self.cannon, self.angle)
        rotated_offset = pivot_offset.rotate(-self.angle)
        blit_center = pivot_point + rotated_offset
        # Draw rotated cannon
        self.window.blit(rotated_cannon, rotated_cannon.get_rect(center=blit_center))
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.key_inputs['left']]:
            self.x -= player_speed * dt
        if keys_pressed[self.key_inputs['right']]:
            self.x += player_speed * dt
        if keys_pressed[self.key_inputs['shoot']]:
            self.shoot() # figure out how to create a shot, and set a limit for how often one can shoot
        if keys_pressed[self.key_inputs['aim_up']]:
            self.angle += aim_speed * dt
        if keys_pressed[self.key_inputs['aim_down']]:
            self.angle -= aim_speed * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = shoot_cooldown
        bullet = shot(self.window, self.cannon_tip_x, self.cannon_tip_y, math.radians(self.angle), black)
        self.bullets = bullet