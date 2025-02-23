import random
from options import options

class block:
    def __init__(self):
        self.init_x = options().block_init_x
        self.x = options().block_x
        self.y = options().block_y
        self.width = options().block_width
        self.height = options().block_height
        self.color_min = options().block_color_min
        self.color_max = options().block_color_max

    def matrix(self):
        blocks = []
        for k in range(5):
            self.y += self.height + 15
            self.x = self.init_x
            for i in range(10):
                self.x += self.width + 15
                color = (random.randint(self.color_min, self.color_max), random.randint(self.color_min, self.color_max), random.randint(self.color_min, self.color_max))
                rect = (self.x, self.y, self.width, self.height)
                blocks.append((color, rect))
        return blocks