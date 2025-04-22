from enum import Enum, auto

class Scene_type(Enum):
    """Available scene types."""
    MENU = auto()
    GAME = auto()
    OPTIONS = auto()
    GAME_OVER = auto()