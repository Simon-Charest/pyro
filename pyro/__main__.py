from math import sqrt
from pygame import (
    init, K_a, K_c, K_d, K_e, K_DOWN, K_ESCAPE, K_LEFT, K_q, K_RETURN, K_RIGHT, K_SPACE, K_s, K_UP,
    K_w, K_z, KEYDOWN, QUIT, quit, Rect, Surface
)
from pygame.display import flip, set_caption, set_mode
from pygame.draw import circle, line, polygon, rect
from pygame.event import Event, get
from pygame.time import Clock
from random import choice, randint

# Pyro
from constant import *
from projectile import Projectile


def main() -> None:
    # Initialize Pygame
    init()

    # Set up screen
    set_caption(TITLE)
    screen: Surface = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define walls
    left_wall: Rect = Rect(0, 0, WALL_WIDTH, SCREEN_HEIGHT)
    right_wall: Rect = Rect(SCREEN_WIDTH - WALL_WIDTH, 0, WALL_WIDTH, SCREEN_HEIGHT)
    top_wall: Rect = Rect(0, 0, SCREEN_WIDTH, WALL_HEIGHT)
    bottom_wall: Rect = Rect(0, SCREEN_HEIGHT - WALL_HEIGHT, SCREEN_WIDTH, WALL_HEIGHT)

    # Set up player
    player_x: int = SCREEN_WIDTH // 2
    player_y: int = SCREEN_HEIGHT // 2
    
    # Generate and draw random opponents
    opponent_x: int
    opponent_y: int
    opponent_height: int
    opponent: list[tuple[int, int]]
    opponents: list = []
    clock: Clock = Clock()

    for _ in range(OPPONENT_COUNT):
        opponent_x, opponent_y = get_coordinates(left_wall, right_wall, top_wall, bottom_wall)
        opponent_height = int(OPPONENT_SIDE_LENGTH * (3 ** 0.5) / 2)
        opponent = [
            (opponent_x, opponent_y - opponent_height // 2),
            (opponent_x - OPPONENT_SIDE_LENGTH // 2, opponent_y + opponent_height // 2),
            (opponent_x + OPPONENT_SIDE_LENGTH // 2, opponent_y + opponent_height // 2)
        ]
        opponents.append(opponent)

    # Main game loop
    running: bool = True
    event: Event
    projectiles: list[Projectile] = []
    projectile: Projectile
    opponents: list[tuple[int, int]]
    player_direction: tuple[int, int] = (1, 0)
    x: int
    y: int

    while running:
        # Handle events
        for event in get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key in [K_ESCAPE]:
                    running = False

                # Handle player movement
                elif event.key in [K_UP, K_w] and player_y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y -= PLAYER_SPEED
                    player_direction = (0, -1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_DOWN, K_s] and player_y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y += PLAYER_SPEED
                    player_direction = (0, 1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_LEFT, K_a] and player_x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_x -= PLAYER_SPEED
                    player_direction = (-1, 0)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_RIGHT, K_d] and player_x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_x += PLAYER_SPEED
                    player_direction = (1, 0)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_q] and player_y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2 and player_x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y -= PLAYER_SPEED
                    player_x -= PLAYER_SPEED
                    player_direction = (-1, -1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_e] and player_y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2 and player_x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y -= PLAYER_SPEED
                    player_x += PLAYER_SPEED
                    player_direction = (1, -1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_z] and player_y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2 and player_x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y += PLAYER_SPEED
                    player_x -= PLAYER_SPEED
                    player_direction = (-1, 1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_c] and player_y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2 and player_x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player_y += PLAYER_SPEED
                    player_x += PLAYER_SPEED
                    player_direction = (1, 1)
                    move_opponents(opponents, left_wall, right_wall, top_wall, bottom_wall)

                elif event.key in [K_RETURN, K_SPACE]:
                    projectiles.append(Projectile(player_x, player_y, player_direction))

                    for projectile in projectiles:
                        projectile.move()

                # Remove projectiles that are out of the game play area
                projectiles = [projectile for projectile in projectiles if left_wall.right < projectile.x < right_wall.left and top_wall.bottom < projectile.y < bottom_wall.top]

        # Fill screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))

        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Draw walls
        rect(screen, WALL_COLOR, top_wall)
        rect(screen, WALL_COLOR, bottom_wall)
        rect(screen, WALL_COLOR, left_wall)
        rect(screen, WALL_COLOR, right_wall)

        # Draw opponents
        for opponent in opponents:
            polygon(screen, OPPONENT_COLOR, opponent)

        # Draw line indicating player's direction
        line_start = (player_x, player_y)
        line_end = (player_x + player_direction[0] * 30, player_y + player_direction[1] * 30)  # Adjust length as needed
        line(screen, PLAYER_COLOR, line_start, line_end, 2)  # Red line indicating direction

        # Draw and move bullets
        for projectile in projectiles:
            circle(screen, PROJECTILE_COLOR, (int(projectile.x), int(projectile.y)), PROJECTILE_SIZE)

        # Draw player
        circle(screen, PLAYER_COLOR, (player_x, player_y), PLAYER_SIZE)

        # Update display
        flip()

        # Cap frame rate
        clock.tick(60)

    # Quit Pygame
    quit()


def get_coordinates(left_wall: Rect, right_wall: Rect, top_wall: Rect, bottom_wall: Rect) -> tuple[int, int]:
    """Generate random coordinates."""

    x_grid: int = randint(left_wall.right + PLAYER_SIZE // 2, right_wall.left - PLAYER_SIZE // 2)
    y_grid: int = randint(top_wall.bottom + PLAYER_SIZE // 2, bottom_wall.top - PLAYER_SIZE // 2)

    # Snap to grid
    x: int = round(x_grid / GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    y: int = round(y_grid / GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2

    return x, y


def move_opponents(opponents: list, left_wall: Rect, right_wall: Rect, top_wall: Rect, bottom_wall: Rect) -> None:
    """Move opponents randomly within the play area."""

    opponent: list
    dx: int
    dy: int
    x: int
    y: int

    # Move opponents randomly
    for opponent in opponents:
        dx, dy = choice([(0, GRID_SIZE), (0, -GRID_SIZE), (GRID_SIZE, 0), (-GRID_SIZE, 0)])
        new_opponent_positions = [(x + dx, y + dy) for x, y in opponent]

        # Check if the new positions are within the play area
        for x, y in new_opponent_positions:
            if not (left_wall.right < x < right_wall.left and top_wall.bottom < y < bottom_wall.top):
                # If opponent tries to move outside the play area, revert the movement
                break

            else:
                # If all new positions are within the play area, update the opponent's position
                opponent[:] = new_opponent_positions


if __name__ == "__main__":
    main()
