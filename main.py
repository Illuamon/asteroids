import pygame
import sys
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = 60
    score = 0

    print("Starting Asteroids!")

    the_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    triangle = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color='black')
        dt = the_clock.tick(fps) / 1000

        font = pygame.font.Font(None, 30)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        updatable.update(dt) 
        for item in drawable:
            item.draw(screen)
        
        for item in asteroids:
            if item.check_collisions(triangle):
                print("Game over!")
                print(f"Score was: {score}")
                sys.exit()
        
        for item in asteroids:
            for bullet in shots:
                if item.check_collisions(bullet):
                    item.split()
                    bullet.kill()
                    score += 1

        pygame.display.flip()

if __name__ == "__main__":
    main()
