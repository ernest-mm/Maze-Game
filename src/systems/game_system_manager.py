from typing import Dict, Any, Optional

"""
In a game, you might have various systems that handle specific game mechanics, for example:
Combat_system: Handles attacks, damage, defense
Inventory_system: Manages the player's inventory (especially for your knapsack mechanics)
Maze_generation_system: Handles the DFS maze generation
Path_finding_system: Manages BFS for shortest path calculations
Collection_system: Handles the munitions collection modes (greedy and dynamic programming)
The System_registry would be used to:
Register these systems when they're created
Access them when needed from different parts of the game
Ensure only one instance of each system exists (like a service locator)
"""

class Game_system_manager:
    """Responsible for managing game systems."""
    def __init__(self) -> None:
        self.__systems: Dict[str, Any] = {}
    
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
