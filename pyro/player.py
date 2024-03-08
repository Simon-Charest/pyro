from pygame.draw import circle, line

# Pyro
from constant import *


class Player:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.direction = (1, 0)  # Default direction
        self.lives = 3  # Set initial lives
    
    def move(self, x: int, y: int, speed: int = PLAYER_SPEED):
        # Set direction
        self.direction = (x, y)

        # Move
        self.x += speed * x
        self.y += speed * y
    
    def draw(self, screen):
        # Draw player
        circle(screen, self.color, (self.x, self.y), self.size)

        # Draw line indicating player's direction
        line_start = (self.x, self.y)
        line_end = (self.x + self.direction[0] * 30, self.y + self.direction[1] * 30)
        line(screen, self.color, line_start, line_end, 2)

    def reduce_lives(self):
        self.lives -= 1
