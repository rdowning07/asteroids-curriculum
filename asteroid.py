import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_RADIUS, ASTEROID_MIN_RADIUS


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
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        new_radius = self.radius // 2
        asteroid_1 = Asteroid(self.x, self.y, new_radius)
        asteroid_2 = Asteroid(self.x, self.y, new_radius)
        return [asteroid_1, asteroid_2]

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.wrap()
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    @staticmethod
    def spawn():
        #calculate random edge position
        #return a new asteroid at that position
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            x = random.randint(0, SCREEN_WIDTH)
            y = 0
        elif edge == 'bottom':
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT
        elif edge == 'left':
            x = 0
            y = random.randint(0, SCREEN_HEIGHT)
        else:  # edge == 'right'
            x = SCREEN_WIDTH
            y = random.randint(0, SCREEN_HEIGHT)
        return Asteroid(x, y, ASTEROID_RADIUS)
    