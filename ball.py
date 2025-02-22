import math

class ball:
    def __init__(self, boundary_w, boundary_h):
        self.boundary_w = boundary_w
        self.boundary_h = boundary_h
        self.colour = (0,0,255)
        self.x = boundary_w / 2
        self.y = boundary_h / 2
        self.radius = 10
        self.speed_x = 3
        self.speed_y = 3
        self.alive = False

    def position(self):
        return (self.x, self.y)
    
    def handle_boundary_collision(self):
        if self.x - self.radius <= 0:
            self.speed_x = math.fabs(self.speed_x)
        if self.y - self.radius <= 0:
            self.speed_y = math.fabs(self.speed_y)
        if self.x + self.radius >= self.boundary_w:
            self.speed_x *= -1
        if self.y + self.radius >= self.boundary_h:
            self.speed_y *= -1
    
    def launch(self):
        self.alive = True

    def move(self):
        if self.alive == True:
            self.x += self.speed_x
            self.y += self.speed_y
            self.handle_boundary_collision()
