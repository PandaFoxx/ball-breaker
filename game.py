import pygame
import sys
from paddle import paddle
from ball import ball

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Breakout")

player = paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
bullet = ball(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    # Draw Player
    pygame.draw.rect(screen, player.colour, player.rect())

    # Draw Ball
    pygame.draw.circle(screen, bullet.colour, bullet.position(), bullet.radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()