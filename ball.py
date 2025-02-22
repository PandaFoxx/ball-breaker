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
    
    def reset(self):
        self.x = self.boundary_w / 2
        self.y = self.boundary_h / 2

    def launch(self):
        self.reset()
        self.alive = True

    def die(self, player_rect):
        self.x = player_rect[0] + player_rect[2] / 2
        self.y = player_rect[1] - self.radius
        self.alive = False
    
    def handle_boundary_collision(self, player_rect):
        left = self.x - self.radius
        top = self.y - self.radius
        right = self.x + self.radius
        bottom = self.y + self.radius

        if left <= 0:
            self.speed_x = math.fabs(self.speed_x)

        if top <= 0:
            self.speed_y = math.fabs(self.speed_y)

        if right >= self.boundary_w:
            self.speed_x *= -1

        #paddle
        if bottom >= player_rect[1]:
            if left >= player_rect[0] and right <= (player_rect[0] + player_rect[2]):
                self.speed_y *= -1
            else:
                self.die(player_rect)
    
    def move(self, player_rect):
        if self.alive == True:
            self.x += self.speed_x
            self.y += self.speed_y
            self.handle_boundary_collision(player_rect)
