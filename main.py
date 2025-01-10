import sys
import pygame
import pygame.freetype
from constants import * 
from player import Player
from asteroid import Asteroid
from AsteroidField import *
from circleshape import CircleShape
from shot import Shot
from powerups import PowerUp, FireRate


def main():
    pygame.init()
    pygame.freetype.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_font = pygame.freetype.SysFont("Comic Sans MS", 30)
    player_score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    PowerUp.containers = (powerups, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    powerup = FireRate(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if bullet.check_collision(asteroid):
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        player_score += 100
                    asteroid.split()
                    bullet.kill()
                    

        for pu in powerups:
            if pu.check_collision(player):
                player.timer_speed_up -= 0.5

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        game_font.render_to(screen, (10, 10), f"SCORE : {player_score}", "white")

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()