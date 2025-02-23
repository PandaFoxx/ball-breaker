import pygame
from models.options import options

class paddle:
    def __init__(self):
        self.boundary_w = options().screen_width
        self.boundary_h = options().screen_height
        self.width = options().player_width
        self.height = options().player_height
        self.color = options().player_color
        self.x = options().player_x
        self.y = options().player_y
        self.speed = options().player_speed

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move_left(self):
        if self.x > 2:
            self.x -= self.speed

    def move_right(self):
        if (self.x + self.width) < self.boundary_w:
            self.x += self.speed
