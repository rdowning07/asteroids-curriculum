import pygame
import math
from bullet import Bullet
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

THRUST = 200
SHOOT_COOLDOWN = 0.3
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.angle = 0
        self.size = 20
        self.radius = 15

        self.velocity_x = 0.0
        self.velocity_y = 0.0

        self.shoot_cooldown = 0.0

    def rotate(self, direction):
        self.angle += direction

    def shoot(self, dt):
        self.shoot_cooldown -= dt
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = SHOOT_COOLDOWN
            nose_x = self.x + math.cos(math.radians(self.angle - 90)) * self.size
            nose_y = self.y + math.sin(math.radians(self.angle - 90)) * self.size
            return Bullet(nose_x, nose_y, self.angle)
        return None

    def get_points(self):
        # Define the ship's points relative to its center
        points = [
            (0, -self.size),  # Nose
            (-self.size / 2, self.size / 2),  # Left wing
            (self.size / 2, self.size / 2)   # Right wing
        ]

        # Rotate and translate the points based on the ship's angle and position
        rotated_points = []
        for px, py in points:
            rotated_x = px * math.cos(math.radians(self.angle)) - py * math.sin(math.radians(self.angle))
            rotated_y = px * math.sin(math.radians(self.angle)) + py * math.cos(math.radians(self.angle))
            final_x = self.x + rotated_x
            final_y = self.y + rotated_y
            rotated_points.append((final_x, final_y))
        return rotated_points

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.get_points())

    def wrap(self):
        if self.x > SCREEN_WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = SCREEN_WIDTH
        if self.y > SCREEN_HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT

    #update(self,dt) method that addes velocity_x *dt to self.x and velocity_y * dt to self.y
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.wrap()

    #thrust(self, dt) method that adds THRUST * cos(angle) * dt to velocity_x and THRUST * sin(angle) * dt to velocity_y
    # math.cos(math.radians(self.angle - 90))
    # math.sin(math.radians(self.angle - 90))
    def thrust(self, dt):
        self.velocity_x += THRUST * math.cos(math.radians(self.angle - 90)) * dt
        self.velocity_y += THRUST * math.sin(math.radians(self.angle - 90)) * dt

