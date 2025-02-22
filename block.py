import random

class block:
    def __init__(self):
        self.init_x = 10
        self.init_y = 10
        self.x = 10
        self.y = 10
        self.width = 50
        self.height = 20
        self.color_min = 128
        self.color_max = 255

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