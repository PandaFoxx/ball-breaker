import pygame
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
        self.reset_position(player.left, player.top, player.width)
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
        if bottom >= player.top:
            if right >= player.left and left <= (player.left + player.width):
                self.speed_y *= -1
            else:
                self.die()

        # collide with brick
        for brick in bricks:
            # Example brick data: (Color(r, g, b), Rect(x, y, w, h))
            block = brick[1]

            closest_x = max(block.left, min(self.x, block.right))
            closest_y = max(block.top, min(self.y, block.bottom))

            dx = self.x - closest_x
            dy = self.y - closest_y
            distance = math.hypot(dx, dy)

            if distance <= self.radius:
                if brick in bricks:
                    bricks.remove(brick)
                if dx >= dy:
                    self.speed_x *= -1
                else:
                    self.speed_y *= -1

    def move(self, player, bricks):
        if self.alive == True:
            self.x += self.speed_x
            self.y += self.speed_y
            self.handle_collisions(player, bricks)

    def move_with_player(self, player):
        if self.alive == False:
            self.reset_position(player.left, player.top, player.width)
