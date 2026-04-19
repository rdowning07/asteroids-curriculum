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

def check_bullet_asteroid_collisions(bullets, asteroids):
    # loop over copies of both lists
    # calculate distance between each bullet and each asteroid
    # if distance < bullet.radius + asteroid.radius, remove both
    for bullet in bullets[:]:
        for asteroid in asteroids[:]:
            dx = bullet.x - asteroid.x
            dy = bullet.y - asteroid.y
            distance = (dx**2 + dy**2) ** 0.5
            if distance < bullet.radius + asteroid.radius:
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                break  # stop checking this bullet against other asteroids

def check_ship_asteroid_collisions(ship, asteroids):
    # loop over asteroids
    # calculate distance between ship and asteroid
    # if distance < ship.radius + asteroid.radius, return True
    # return False at the end
    for asteroid in asteroids:
        dx = ship.x - asteroid.x
        dy = ship.y - asteroid.y
        distance = (dx**2 + dy**2) ** 0.5
        if distance < ship.radius + asteroid.radius:
            return True
    return False

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
        bullet = ship.shoot(dt)
        if bullet is not None:
            bullets.append(bullet)

    ship.update(dt)
    for asteroid in asteroids:
        asteroid.update(dt)
    for bullet in bullets:
        bullet.update(dt)

    check_bullet_asteroid_collisions(bullets, asteroids)
    if check_ship_asteroid_collisions(ship, asteroids):
        running = False

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
