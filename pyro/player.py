from pygame import Surface
from pygame.draw import circle, line

# Pyro
from constant import *


class Player:
    def __init__(
        self,
        x: int = PLAYER_X,
        y: int = PLAYER_Y,
        size: int = PLAYER_SIZE,
        color: tuple[int, int, int] = PLAYER_COLOR,
        direction: tuple[int, int] = PLAYER_DIRECTION,
        speed: int = PLAYER_SPEED,
        lives: int = PLAYER_LIVES
    ) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.direction = direction
        self.speed = speed
        self.lives = lives
    
    def move(self, x: int, y: int) -> None:
        # Set direction
        self.direction = (x, y)

        # Move
        self.x += self.speed * x
        self.y += self.speed * y
    
    def draw(self, surface: Surface) -> None:
        # Draw player
        circle(surface, self.color, (self.x, self.y), self.size)

        # Draw line indicating player's direction
        line_start = (self.x, self.y)
        line_end = (self.x + self.direction[0] * PLAYER_WEAPON_SIZE, self.y + self.direction[1] * PLAYER_WEAPON_SIZE)
        line(surface, self.color, line_start, line_end, 2)

    def reduce_lives(self) -> None:
        self.lives -= 1
