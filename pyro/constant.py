# Colors
BLACK_COLOR: tuple[int, int, int] = (0, 0, 0)
BLUE_COLOR: tuple[int, int, int] = (0, 192, 255)
GRAY_COLOR: tuple[int, int, int] = (32, 32, 32)
RED_COLOR: tuple[int, int, int] = (255, 64, 64)
WHITE_COLOR: tuple[int, int, int] = (255, 255, 255)

# Player
PLAYER_COLOR: tuple[int, int, int] = BLUE_COLOR
PLAYER_SPEED: int = int(800 / 15)
PLAYER_SIZE: int = int(PLAYER_SPEED / 3)

# Projectile
PROJECTILE_COLOR: tuple[int, int, int] = PLAYER_COLOR
PROJECTILE_SIZE: int = PLAYER_SIZE / 5
PROJECTILE_SPEED: int = PLAYER_SPEED

# Opponent
OPPONENT_COLOR: tuple[int, int, int] = RED_COLOR
OPPONENT_COUNT: int = 3
OPPONENT_SIDE_LENGTH: int = 2 * PLAYER_SIZE

# Gameplay area
TITLE: str = "Pyro"
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
BACKGROUND_COLOR: tuple[int, int, int] = BLACK_COLOR
WALL_COLOR: tuple[int, int, int] = WHITE_COLOR
WALL_HEIGHT: int = 5
WALL_WIDTH: int = WALL_HEIGHT
GRID_COLOR: tuple[int, int, int] = GRAY_COLOR
GRID_SIZE: int = int(PLAYER_SPEED)
