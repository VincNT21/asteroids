import pygame
from circleshape import *
from constants import *

class PowerUp (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.timer = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, 20, 20))

class FireRate (PowerUp):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = "red"
        


