import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


ASTEROID_SPEED = 100

class Asteroid:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.velocity_x = random.uniform(-1, 1) * ASTEROID_SPEED
        self.velocity_y = random.uniform(-1, 1) * ASTEROID_SPEED
    
    def wrap(self):
        if self.x > SCREEN_WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = SCREEN_WIDTH
        if self.y > SCREEN_HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.wrap()
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)