from pygame import Rect, Surface
from pygame.draw import polygon
from random import choice

# Pyro
from constant import *


class Opponent:
    x: int
    y: int
    size: int
    color: tuple[int, int, int]
    direction: tuple[int, int]

    def __init__(self, x: int, y: int, size: int = OPPONENT_SIZE, color: tuple[int, int, int] = OPPONENT_COLOR) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.direction = self.get_random_direction()  # Set random direction
    
    def move(self, left_wall: Rect, right_wall: Rect, top_wall: Rect, bottom_wall: Rect) -> None:
        # Set random direction
        self.direction = self.get_random_direction()
        
        # Set destination tile
        new_x: int = self.x + self.direction[0]
        new_y: int = self.y + self.direction[1]

        # If not hitting a wall
        if left_wall.right < new_x < right_wall.left and top_wall.bottom < new_y < bottom_wall.top:
            # Move
            self.x = new_x
            self.y = new_y

    def get_random_direction(self) -> list[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
        return choice([(0, GRID_SIZE), (0, -GRID_SIZE), (GRID_SIZE, 0), (-GRID_SIZE, 0)])
    
    def draw(self, surface: Surface) -> None:
        points: list[tuple[int, int]] = [
            (self.x, self.y - self.size // 2),
            (self.x - self.size // 2, self.y + self.size // 2),
            (self.x + self.size // 2, self.y + self.size // 2)
        ]
        polygon(surface, self.color, points)
