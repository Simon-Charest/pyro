TITLE: str = "Pyro"
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
BACKGROUND_COLOR: tuple[int, int, int] = (255, 255, 255)  # White

WALL_COLOR: tuple[int, int, int] = (0, 0, 0)  # Black
WALL_HEIGHT: int = 10
WALL_WIDTH: int = WALL_HEIGHT

PLAYER_COLOR: tuple[int, int, int] = (0, 0, 255)  # Blue
PLAYER_SPEED: int = int(800 / 15)
PLAYER_SIZE: int = int(PLAYER_SPEED / 3)

GRID_COLOR: tuple[int, int, int] = (200, 200, 200)  # Gray
GRID_SIZE: int = int(PLAYER_SPEED)

OPPONENT_COLOR: tuple[int, int, int] = (255, 0, 0)  # Red
OPPONENT_COUNT: int = 3
OPPONENT_SIDE_LENGTH: int = 2 * PLAYER_SIZE
