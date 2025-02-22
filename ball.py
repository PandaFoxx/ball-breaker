class ball:
    def __init__(self, boundary_w, boundary_h):
        self.boundary_w = boundary_w
        self.boundary_h = boundary_h
        self.colour = (0,0,255)
        self.x = boundary_w / 2
        self.y = boundary_h / 2
        self.radius = 10

    def position(self):
        return (self.x, self.y)