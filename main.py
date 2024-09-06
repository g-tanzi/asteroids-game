import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Sprites
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        # Listen for close game windoe event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update Objects
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                raise SystemExit(0)
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()

        # Paint blackground blacl
        screen.fill("black")

        # Draw Objects
        for obj in drawable:
            obj.draw(screen)

        # Updates the actual screen
        pygame.display.flip()

        # Limits Framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
