import pygame
import sys
import random
from paddle import paddle
from ball import ball
from options import options

pygame.init()

screen = pygame.display.set_mode((options().screen_width, options().screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption(options().screen_caption)

player = paddle()
bullet = ball()

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
    brick_y = -25
    for a in range(5):
        brick_y += 35
        brick_x = 10
        for b in range(12):
            pygame.draw.rect(screen, (random.randint(128,255),random.randint(128,255),random.randint(128,255)), (brick_x, brick_y, 50, 20))
            brick_x += 65

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