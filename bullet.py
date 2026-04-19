import pygame
import random
from asteroid import ASTEROID_SPEED
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


BULLET_SPEED = 100

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.radius = 5
        self.angle = angle

        self.velocity_x = pygame.math.Vector2(BULLET_SPEED, 0).rotate(self.angle).x
        self.velocity_y = pygame.math.Vector2(BULLET_SPEED, 0).rotate(self.angle).y
    
    is offscreen(self):
        return self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT

    update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
    
    draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
    