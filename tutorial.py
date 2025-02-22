import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -=5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()