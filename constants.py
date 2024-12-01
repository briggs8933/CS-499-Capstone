# constants.py

"""
Defines constants used throughout the game.
"""

# Screen dimensions
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

# Room dimensions
ROOM_WIDTH: int = 150
ROOM_HEIGHT: int = 100

# Text box dimensions
TEXT_BOX_HEIGHT: int = 150
TEXT_BOX_WIDTH: int = SCREEN_WIDTH
TEXT_BOX_X: int = 0
TEXT_BOX_Y: int = SCREEN_HEIGHT - TEXT_BOX_HEIGHT

# Colors (RGB)
WHITE: tuple = (255, 255, 255)
BLACK: tuple = (0, 0, 0)
CLEAN_COLOR: tuple = (0, 255, 0)    # Green for clean rooms
DIRTY_COLOR: tuple = (255, 0, 0)    # Red for dirty rooms

# Font settings
FONT_NAME: str = 'Arial'
FONT_SIZE: int = 20
FONT_COLOR: tuple = WHITE

# Frame rate
FPS: int = 60