"""Define enums and constants for the project."""
from enum import Enum, auto


class MenuOption(Enum):
    """Enum representing options in the main menu.

    Attributes:
        PLAY: Option to start the game.
        HIGH_SCORE: Option to view the high score.
        QUIT: Option to quit the game.
    """

    PLAY = auto()
    HIGH_SCORE = auto()
    QUIT = auto()
