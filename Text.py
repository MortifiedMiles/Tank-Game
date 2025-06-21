import pygame
class simple_text():
    def __init__(self, window, text, x, y, color, font = 50, font_size = 'Comic Sans MS'):
        self.window = window
        self._text = text
        self._x = x
        self._y = y
        self.color = color
        self._text = text

        self._font = pygame.font.SysFont(font, font_size)
        self.textSurface = self._font.render(self._text, True, self.color)
    
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
    def pos(self):
        return (self._x, self._y)
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.textSurface = self._font.render(self._text, True, self.color)


    def print_text(self):
        self.window.blit(self.textSurface, self.pos)