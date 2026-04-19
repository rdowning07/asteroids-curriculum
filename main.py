import pygame
from ship import Ship
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_COUNT


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

#set up the clock for a decent framerate
clock = pygame.time.Clock()
ship = Ship(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
asteroids = [Asteroid.spawn() for _ in range(ASTEROID_COUNT)]
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
    for asteroid in asteroids:
        asteroid.update(dt)

    screen.fill((0, 0, 0))
    ship.draw(screen)
    for asteroid in asteroids:
        asteroid.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()
