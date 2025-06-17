import pygame
import math
from constants import *
from Shot import shot

class tank():
    def __init__(self, window, x_start = 50, y_start = 400, angle_start = 80, key_inputs = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'aim_up': pygame.K_UP, 'aim_down': pygame.K_DOWN, 'shoot': pygame.K_SPACE}):
        self._x = x_start
        self._y = y_start
        self.window = window
        self.key_inputs = key_inputs
        self._angle = angle_start
        self.shoot_timer = 0
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
        pygame.draw.rect(self.window, player_color, (self._x, self._y, player_width, player_height), 1)

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

        # Draw angle highlight
        pygame.draw.circle(self.window, (255, 255, 255),
                           (self.x + shot_speed * math.cos(math.radians(self.angle))
                            ,self.y + shot_speed * math.sin(math.radians(self.angle))), 5)
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.key_inputs['left']]:
            self.x -= player_speed * dt
        if keys_pressed[self.key_inputs['right']]:
            self.x += player_speed * dt
        if keys_pressed[self.key_inputs['shoot']]:
            print("space")
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