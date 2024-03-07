# Pyro
from constant import *


class Projectile:
    def __init__(self, x: int, y: int, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        self.x += self.direction[0] * PROJECTILE_SPEED
        self.y += self.direction[1] * PROJECTILE_SPEED
