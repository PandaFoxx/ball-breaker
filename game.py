import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Breakout")

class paddle:
    def __init__(self, boundary_w, boundary_h):
        self.width = 200
        self.height = 15
        self.colour = (0,255,0)
        self.x = (boundary_w / 2) - (self.width / 2)
        self.y = boundary_h - (self.height * 2)

    def rect(self):
        return (self.x, self.y, self.width, self.height)

player = paddle(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Player
    pygame.draw.rect(screen, player.colour, player.rect())

    pygame.display.flip()

pygame.quit()
sys.exit()