import pygame
import math
import random
from options import options

class block:
    def __init__(self):
        self.screen_width = options().screen_width
        self.init_x = options().block_init_x
        self.x = options().block_x
        self.y = options().block_y
        self.width = options().block_width
        self.height = options().block_height
        self.gap = options().block_gap
        self.rows = options().block_rows
        self.color_min = options().block_color_min
        self.color_max = options().block_color_max

    def matrix(self):
        blocks = []
        h_range = math.floor((self.screen_width - self.init_x) / (self.width + self.gap))
        for k in range(self.rows):
            self.y += self.height + self.gap
            self.x = self.init_x
            for i in range(h_range - 2):
                self.x += self.width + self.gap
                color = (random.randint(self.color_min, self.color_max), random.randint(self.color_min, self.color_max), random.randint(self.color_min, self.color_max))
                rect = pygame.Rect(self.x, self.y, self.width, self.height)
                blocks.append((color, rect))
        return blocks