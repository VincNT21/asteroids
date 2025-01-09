import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        new_vect_1 = self.velocity.rotate(random_angle)
        new_vect_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = new_vect_1 * 1.2
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2.velocity = new_vect_2 * 1.2

