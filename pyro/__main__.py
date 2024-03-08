from pygame import (
    KEYDOWN, K_DOWN, K_ESCAPE, K_LEFT, K_RETURN, K_RIGHT, K_SPACE, K_UP, K_a,
    K_c, K_d, K_e, K_q, K_s, K_w, K_z, QUIT, Rect, Surface, init, quit
)
from pygame.display import flip, set_caption, set_mode
from pygame.draw import circle, line, polygon, rect
from pygame.event import Event, get
from pygame.time import Clock
from random import choice, randint

# Pyro
from constant import *
from opponent import Opponent
from player import Player
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
    player = Player()
    
    # Generate and draw random opponents
    opponents: list[Opponent] = generate_opponents(left_wall, right_wall, top_wall, bottom_wall)

    # Main game loop
    running: bool = True
    event: Event
    projectiles: list[Projectile] = []
    projectile: Projectile
    opponents: list[Opponent]
    opponent: Opponent
    x: int
    y: int
    clock = Clock()

    while running:
        # Handle events
        for event in get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key in [K_ESCAPE]:
                    running = False

                # Handle player movement
                
                # Up
                elif event.key in [K_UP, K_w] and player.y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(0, -1)

                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Down
                elif event.key in [K_DOWN, K_s] and player.y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(0, 1)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Left
                elif event.key in [K_LEFT, K_a] and player.x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(-1, 0)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Right
                elif event.key in [K_RIGHT, K_d] and player.x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(1, 0)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Up left
                elif event.key in [K_q] and player.y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2 and player.x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(-1, -1)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Up right
                elif event.key in [K_e] and player.y - PLAYER_SPEED > top_wall.bottom + PLAYER_SIZE // 2 and player.x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(1, -1)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Down left
                elif event.key in [K_z] and player.y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2 and player.x - PLAYER_SPEED > left_wall.right + PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(-1, 1)
                    
                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Down right
                elif event.key in [K_c] and player.y + PLAYER_SPEED < bottom_wall.top - PLAYER_SIZE // 2 and player.x + PLAYER_SPEED < right_wall.left - PLAYER_SIZE // 2:
                    for projectile in projectiles:
                        projectile.move()
                    
                    player.move(1, 1)

                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Shoot
                elif event.key in [K_RETURN, K_SPACE]:
                    projectiles.append(Projectile(player.x, player.y, player.direction))

                    for projectile in projectiles:
                        projectile.move()

                    for opponent in opponents:
                        opponent.move(left_wall, right_wall, top_wall, bottom_wall)

                # Remove projectiles that are out of the game play area
                projectiles = [projectile for projectile in projectiles if left_wall.right < projectile.x < right_wall.left and top_wall.bottom < projectile.y < bottom_wall.top]

        # Fill screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))

        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Draw player
        player.draw(screen)

        # Draw opponents
        for opponent in opponents:
            opponent.draw(screen)

        # Draw projectiles
        for projectile in projectiles:
            circle(screen, PROJECTILE_COLOR, (int(projectile.x), int(projectile.y)), PROJECTILE_SIZE)

        # Draw walls
        rect(screen, WALL_COLOR, top_wall)
        rect(screen, WALL_COLOR, bottom_wall)
        rect(screen, WALL_COLOR, left_wall)
        rect(screen, WALL_COLOR, right_wall)

        # Update display
        flip()

        # Cap frame rate
        clock.tick(60)

    # Quit Pygame
    quit()


def generate_opponents(left_wall: Rect, right_wall: Rect, top_wall: Rect, bottom_wall: Rect) -> None:
    x: int
    y: int
    opponents: list[Opponent] = []

    for _ in range(OPPONENT_COUNT):
        x, y = get_coordinates(left_wall, right_wall, top_wall, bottom_wall)
        opponents.append(Opponent(x, y))

    return opponents


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
