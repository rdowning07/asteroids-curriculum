import pygame
import random
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


BULLET_SPEED = 100

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.radius = 5
        self.angle = angle

        velocity = pygame.math.Vector2(BULLET_SPEED, 0).rotate(self.angle)
        self.velocity_x = math.cos(math.radians(self.angle - 90)) * BULLET_SPEED
        self.velocity_y = math.sin(math.radians(self.angle - 90)) * BULLET_SPEED
    
    def is_offscreen(self):
        return self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
    