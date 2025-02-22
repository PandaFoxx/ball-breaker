import pygame
import sys
import random
from paddle import paddle
from ball import ball
from options import options
from block import block

pygame.init()

screen = pygame.display.set_mode((options().screen_width, options().screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption(options().screen_caption)

player = paddle()
bullet = ball()
brick = block()

bricks = brick.matrix()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(options().screen_color)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
        bullet.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
        bullet.move_right()
    if keys[pygame.K_SPACE]:
        bullet.launch(player.rect())

    bullet.move(player.rect())

    # Draw Blocks
    for i in bricks:
        pygame.draw.rect(screen, i[0], i[1])

    # Draw Player
    pygame.draw.rect(screen, player.color, player.rect())

    # Draw Ball
    pygame.draw.circle(screen, bullet.color, bullet.position(), bullet.radius)

    # Refresh graphics
    pygame.display.flip()

    # Set framerate
    clock.tick(60)

pygame.quit()
sys.exit()