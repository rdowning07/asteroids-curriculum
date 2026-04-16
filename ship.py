import pygame
import math

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.angle = 0
        self.size = 20

    def rotate(self, direction):
        self.angle += direction

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

