import pygame
from systems.game_manager import Game_manager

class Base_scene:
    def __init__(self, screen: pygame.Surface, game_manager: Game_manager) -> None:
        self._screen = screen
        self._game_manager = game_manager
        self._is_active = True 
    
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle scene-specific events."""
        pass
    
    def update(self) -> None:
        """Update scene logic."""
        pass
    
    def render(self) -> None:
        """Render scene elements."""
        pass 