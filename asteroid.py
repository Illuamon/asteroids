import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color='green', width=2, radius=self.radius, center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = vector1 * 1.2

            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.velocity = vector2 * 1.2