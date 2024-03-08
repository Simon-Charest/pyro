# Pyro
from constant import *


class Projectile:
    x: int
    y: int
    direction: tuple
    
    def __init__(self, x: int, y: int, direction: tuple) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, speed: int = PROJECTILE_SPEED) -> None:
        self.x += speed * self.direction[0]
        self.y += speed * self.direction[1]
