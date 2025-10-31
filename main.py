import pygame
import player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = 60

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    the_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    triangle = player.Player(x, y, PLAYER_RADIUS)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color='black')
        dt = the_clock.tick(fps) / 1000

        triangle.draw(screen)
        triangle.update(dt)

        pygame.display.flip()

if __name__ == "__main__":
    main()
