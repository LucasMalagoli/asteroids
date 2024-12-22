import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
