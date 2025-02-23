import pygame
import sys
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

explosions = []
for i in range(5):
    file = f"assets/explosion-{i}.png"
    try:
        explosions.append(pygame.image.load(file).convert_alpha())
    except:
        print(f"File not found: {file}")

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

    bullet.move(player.rect(), bricks)

    # Draw Blocks
    for i in bricks:
        pygame.draw.rect(screen, i[0], i[1])

    # Draw Player
    pygame.draw.rect(screen, player.color, player.rect())

    # Draw Ball
    pygame.draw.circle(screen, bullet.color, bullet.position(), bullet.radius)

    if bullet.dead == True:
        bullet.dead = False
        for explosion in explosions:
            screen.blit(explosion, (bullet.x - 48, bullet.y - 48))
            pygame.display.flip()
            pygame.time.delay(100)
        bullet.reset_position(player.rect()[0], player.rect()[1], player.rect()[2], player.rect()[3])

    # Refresh graphics
    pygame.display.flip()

    # Set framerate
    clock.tick(60)

pygame.quit()
sys.exit()