import pygame
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = (x, y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color='white', width=2, radius=self.radius, center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt