import math
import random
from options import options

class ball:
    def reset_position(self, player_x, player_y, player_w):
        self.x = player_x + player_w / 2
        self.y = player_y - self.radius

    def __init__(self):
        self.boundary_w = options().screen_width
        self.boundary_h = options().screen_height
        self.color = options().ball_color
        self.radius = options().ball_radius
        self.speed_x = options().ball_speed_x
        self.speed_y = options().ball_speed_y
        self.reset_position(options().player_x, options().player_y, options().player_width)
        self.alive = False # starting condition
        self.dead = False # triggers explosion

    def position(self):
        return (self.x, self.y)

    def init_direction(self):
        r = random.randint(1, 10)
        if r <= 5:
            return -1
        return 1

    def launch(self, player):
        self.speed_x = math.fabs(self.speed_x) * self.init_direction()
        self.reset_position(player[0], player[1], player[2])
        self.alive = True
        self.dead = False

    def die(self):
        self.alive = False
        self.dead = True
    
    def handle_collisions(self, player, bricks):
        left = self.x - self.radius
        top = self.y - self.radius
        right = self.x + self.radius
        bottom = self.y + self.radius

        # collide with screen boundaries
        if top <= 0:
            self.speed_y *= -1
        if left <= 0 or right >= self.boundary_w:
            self.speed_x *= -1

        # collide with paddle
        if bottom >= player[1]:
            if right >= player[0] and left <= (player[0] + player[2]):
                self.speed_y *= -1
            else:
                self.die()

        # collide with brick
        for brick in bricks:
            # Example brick data: ((229, 235, 234), (595, 80, 50, 20))
            brick_left = brick[1][0]
            brick_top = brick[1][1]
            brick_right = brick[1][0] + brick[1][2]
            brick_bottom = brick[1][1] + brick[1][3]

            # fun lil power up that deletes all blocks in path
            # if left <= brick_right and right >= brick_left and bottom >= brick_top and top <= brick_bottom:
            #     bricks.remove(brick)
                
            if left <= brick_right and right > brick_left and bottom > brick_top and top < brick_bottom:
                if brick in bricks:
                    bricks.remove(brick)
                    self.speed_x *= -1
                
            if right >= brick_right and left < brick_right and bottom > brick_top and top < brick_bottom:
                if brick in bricks:
                    bricks.remove(brick)
                    self.speed_x *= -1

            if top <= brick_bottom and bottom > brick_top and left < brick_right and right > brick_left:
                if brick in bricks:
                    bricks.remove(brick)
                    self.speed_y *= -1

            if bottom >= brick_top and top < brick_bottom and left < brick_right and right > brick_left:
                if brick in bricks:
                    bricks.remove(brick)
                    self.speed_y *= -1

        
    
    def move(self, player, bricks):
        if self.alive == True:
            self.x += self.speed_x
            self.y += self.speed_y
            self.handle_collisions(player, bricks)

    def move_with_player(self, player):
        if self.alive == False:
            self.reset_position(player[0], player[1], player[2])
