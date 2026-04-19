import pygame
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_COUNT


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

#set up the clock for a decent framerate
clock = pygame.time.Clock()
ship = Ship(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
asteroids = [Asteroid.spawn() for _ in range(ASTEROID_COUNT)]
bullets = []
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

    if keys[pygame.K_SPACE]:
        bullets.append(ship.shoot())
        
    ship.update(dt)
    for asteroid in asteroids:
        asteroid.update(dt)
    for bullet in bullets:
        bullet.update(dt)

    for bullet in bullets[:]:       # [:] makes a copy to iterate over
        if bullet.is_offscreen():
            bullets.remove(bullet)  # ← modifies the original, safe

    screen.fill((0, 0, 0))
    ship.draw(screen)
    for asteroid in asteroids:
        asteroid.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()
