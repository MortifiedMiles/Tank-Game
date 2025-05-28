from pygame import *
import math

class shot():
    def __init__(self, window, x_start, y_start, dt, initial_velocity, angle, color = (155, 155, 155), gravity = -9.8, radius = 10):
        self.window = window
        self.radius = radius
        self._x = x_start
        self._y = y_start
        self._color = color
        self.start_time = dt
        self.velocity = initial_velocity
        self.angle = angle
        self.gravity = gravity
    
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
    
    def update(self, dt):
        self.time_difference = dt - self.start_time
        if self.velocity > 0:
            x_displacement = self.velocity * math.cos(self.angle) * self.time_difference
            y_displacement = self.velocity * math.sin(self.angle) * self.time_difference + (self.gravity * self.time_difference * self.time_difference)/2

            self.x += x_displacement
            self.y -= y_displacement

            if self.y >= 600 - self.radius:
                self.velocity = 0
                self.y = 600 - self.radius


    def draw(self):
        draw.circle(self.window, self._color, self.pos, self.radius)