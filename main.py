import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Listen for close game windoe event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update player position
        player.update(dt)

        # Objects to draw to screen
        screen.fill("black")
        player.draw(screen)

        # Updates the actual screen
        pygame.display.flip()

        # Limits Framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
