import pygame
import math
from ship import Ship

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

#set up the clock for a decent framerate
clock = pygame.time.Clock()
ship = Ship(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

dt = 0.0

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        ship.rotate(5)
    if keys[pygame.K_LEFT]:
        ship.rotate(-5)

    if keys[pygame.K_UP]:
        ship.thrust(dt)
        
    ship.update(dt)

    screen.fill((0, 0, 0))
    ship.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()
