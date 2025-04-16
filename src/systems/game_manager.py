from typing import Dict, Any, Optional
from enum import Enum, auto

class Scene_type(Enum):
    """Available scene types."""
    MENU = auto()
    GAME = auto()
    OPTIONS = auto()
    GAME_OVER = auto()

class Game_manager:
    def __init__(self) -> None:
        self.__game_state: Dict[str, Any] = {
            "score": 0,
            "health": 100,
            "current_scene": Scene_type.MENU,
            "running": True
        }
        self.__systems: Dict[str, Any] = {}
    
    def get_state(self, key: str, default: Any = None) -> Any:
        """Get value from game state.
        
        Args:
            key: State key to retrieve
            default: Default value to return if key doesn't exist
            
        Returns:
            Value associated with key, or default if key doesn't exist
        """
        try:
            return self.__game_state[key]  
        except KeyError:
            if default is not None:
                return default
            raise KeyError(f"Game state key '{key}' not found. Available keys: {list(self.__game_state.keys())}")
    
    def set_state(self, key: str, value: Any) -> None:
        """Set value in game state.
        
        Args:
            key: State key to set
            value: Value to set
        """
        self.__game_state[key] = value
    
    def register_system(self, name: str, system: Any) -> None:
        """Register a game system.
        
        Args:
            name: System name
            system: System instance
        """
        self.__systems[name] = system
    
    def get_system(self, name: str) -> Optional[Any]:
        """Get a registered system.
        
        Args:
            name: System name to retrieve
            
        Returns:
            System instance if found, None otherwise
        """
        try:
            return self.__systems.get(name) 
        except KeyError:
            raise KeyError(f"System '{name}' not found. Available systems: {list(self.__systems.keys())}")
