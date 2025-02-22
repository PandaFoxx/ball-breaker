import math
from options import options

class ball:
    def reset_position(self, player_x, player_y, player_w, player_h):
        self.x = player_x + player_w / 2
        self.y = player_y - self.radius

    def __init__(self):
        self.boundary_w = options().screen_width
        self.boundary_h = options().screen_height
        self.color = options().ball_color
        self.radius = options().ball_radius
        self.speed_x = options().ball_speed_x
        self.speed_y = options().ball_speed_y
        self.reset_position(options().player_x, options().player_y, options().player_width, options().player_height)
        self.alive = False

    def position(self):
        return (self.x, self.y)

    def launch(self, player):
        self.reset_position(player[0], player[1], player[2], player[3])
        self.alive = True

    def die(self, player):
        self.reset_position(player[0], player[1], player[2], player[3])
        self.alive = False
    
    def handle_collisions(self, player):
        left = self.x - self.radius
        top = self.y - self.radius
        right = self.x + self.radius
        bottom = self.y + self.radius

        # collide with screen boundaries
        if left <= 0:
            self.speed_x = math.fabs(self.speed_x)
        if top <= 0:
            self.speed_y = math.fabs(self.speed_y)
        if right >= self.boundary_w:
            self.speed_x *= -1

        # collide with paddle
        if bottom >= player[1]:
            if left >= player[0] and right <= (player[0] + player[2]):
                self.speed_y *= -1
            else:
                self.die(player)
    
    def move(self, player):
        if self.alive == True:
            self.x += self.speed_x
            self.y += self.speed_y
            self.handle_collisions(player)

    def move_left(self):
        if self.alive == False:
            self.x -= options().player_speed

    def move_right(self):
        if self.alive == False:
            self.x += options().player_speed