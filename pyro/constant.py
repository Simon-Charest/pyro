# Colors
BLACK_COLOR: tuple[int, int, int] = (0, 0, 0)
BLUE_COLOR: tuple[int, int, int] = (0, 192, 255)
GRAY_COLOR: tuple[int, int, int] = (32, 32, 32)
RED_COLOR: tuple[int, int, int] = (255, 64, 64)
WHITE_COLOR: tuple[int, int, int] = (255, 255, 255)

# Gameplay area
TITLE: str = "Pyro"
SURFACE_WIDTH: int = 800
SURFACE_HEIGHT: int = 800
BACKGROUND_COLOR: tuple[int, int, int] = BLACK_COLOR
GRID_COLOR: tuple[int, int, int] = GRAY_COLOR
GRID_SIZE: int = int(800 / 15)
WALL_COLOR: tuple[int, int, int] = WHITE_COLOR
WALL_HEIGHT: int = 5
WALL_WIDTH: int = WALL_HEIGHT

# Player
PLAYER_X: int = SURFACE_WIDTH // 2
PLAYER_Y: int = SURFACE_HEIGHT // 2
PLAYER_SIZE: int = int(GRID_SIZE / 3)
PLAYER_COLOR: tuple[int, int, int] = BLUE_COLOR
PLAYER_DIRECTION: tuple[int, int] = (1, 0)
PLAYER_SPEED: int = GRID_SIZE
PLAYER_LIVES: int = 3
PLAYER_WEAPON_SIZE: int = 1.5 * PLAYER_SIZE

# Projectile
PROJECTILE_SIZE: int = PLAYER_SIZE / 5
PROJECTILE_COLOR: tuple[int, int, int] = PLAYER_COLOR
PROJECTILE_SPEED: int = PLAYER_SPEED

# Opponent
OPPONENT_COLOR: tuple[int, int, int] = RED_COLOR
OPPONENT_COUNT: int = 3
OPPONENT_SIZE: int = 2 * PLAYER_SIZE
