class paddle:
    def __init__(self, boundary_w, boundary_h):
        self.boundary_w = boundary_w-2
        self.boundary_h = boundary_h
        self.width = 200
        self.height = 15
        self.colour = (0,255,0)
        self.x = (boundary_w / 2) - (self.width / 2)
        self.y = boundary_h - (self.height * 2)
        self.speed = 5

    def rect(self):
        return (self.x, self.y, self.width, self.height)
    
    def move_left(self):
        if self.x > 2:
            self.x -= self.speed

    def move_right(self):
        if (self.x + self.width) < self.boundary_w:
            self.x += self.speed
