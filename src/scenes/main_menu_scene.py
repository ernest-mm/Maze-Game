import pygame
from typing import List, Tuple
from scenes.base_scene import Base_scene
from scenes.scene_type import Scene_type
from systems.game_state_manager import Game_state_manager
from utils.font import Font

class Main_menu_scene(Base_scene):
    def __init__(self, screen: pygame.Surface, game_state_manager: Game_state_manager) -> None:
        super().__init__(screen, game_state_manager)
        self.__options: List[str] = ["Start Game", "Options", "Quit"]
        self.__selected: int = 0
        self.__font = Font.get_font(74)
        
        # Colors
        self.__text_color: Tuple[int, int, int] = (255, 255, 255)
        self.__selected_color: Tuple[int, int, int] = (255, 255, 0)
        self.__background_color: Tuple[int, int, int] = (0, 0, 0)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle menu navigation events with keyboard and mouse."""
        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__selected = (self.__selected - 1) % len(self.__options)
            elif event.key == pygame.K_DOWN:
                self.__selected = (self.__selected + 1) % len(self.__options)
            elif event.key == pygame.K_RETURN:
                self.__select_option()
        
        # Mouse controls
        elif event.type == pygame.MOUSEMOTION:
            # Get mouse position
            mouse_x, mouse_y = event.pos
            
            # Check which option the mouse is hovering over
            for i, option in enumerate(self.__options):
                # Calculate text position (same as in render method)
                text_surface = self.__font.render(option, True, self.__text_color)
                pos_x = self._screen.get_width() // 2 - text_surface.get_width() // 2
                pos_y = 200 + i * 100
                
                # Create a rect for hit detection
                option_rect = pygame.Rect(
                    pos_x, 
                    pos_y, 
                    text_surface.get_width(), 
                    text_surface.get_height()
                )
                
                # If mouse is over this option, select it
                if option_rect.collidepoint(mouse_x, mouse_y):
                    self.__selected = i
                    break
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Get mouse position
                mouse_x, mouse_y = event.pos
                
                # Check if click was on the selected option
                text_surface = self.__font.render(
                    self.__options[self.__selected], 
                    True, 
                    self.__text_color
                )
                pos_x = self._screen.get_width() // 2 - text_surface.get_width() // 2
                pos_y = 200 + self.__selected * 100
                
                option_rect = pygame.Rect(
                    pos_x, 
                    pos_y, 
                    text_surface.get_width(), 
                    text_surface.get_height()
                )
                
                if option_rect.collidepoint(mouse_x, mouse_y):
                    self.__select_option()
    
    def __select_option(self) -> None:
        """Handle menu option selection."""
        selected_option = self.__options[self.__selected]
        
        if selected_option == "Start Game":
            self._game_state_manager.set_state("current_scene", Scene_type.GAME)
        elif selected_option == "Options":
            self._game_state_manager.set_state("current_scene", Scene_type.OPTIONS)
        elif selected_option == "Quit":
            self._game_state_manager.set_state("running", False)
    
    def render(self) -> None:
        """Render menu options."""
        self._screen.fill(self.__background_color)
        
        screen_center_x = self._screen.get_width() // 2
        
        for i, option in enumerate(self.__options):
            color = self.__selected_color if i == self.__selected else self.__text_color
            text_surface = self.__font.render(option, True, color)
            pos_x = screen_center_x - text_surface.get_width() // 2
            pos_y = 200 + i * 100
            self._screen.blit(text_surface, (pos_x, pos_y)) 