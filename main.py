import sys
import pygame
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from constants import *
from player import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Delta Time: change in time per every frame update.
    dt = 0
    clock = pygame.time.Clock()

    # creating a groups to manage multiple sprites:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=(0,0,0))

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")

            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        # refreshes screen
        pygame.display.flip()

        # pauses the game until 1/60th of a second has passed.
        current_dt_seconds = clock.tick(60)
        dt = current_dt_seconds / 1000


# ensures that the main function only runs if this file is direcly run.
if __name__ == "__main__":
    main()
