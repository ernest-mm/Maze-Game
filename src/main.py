#!/usr/bin/env python3
"""
Main entry point for the Maze Game.
"""
import pygame
import sys
from utils.display_resolution import Display_resolution
from scenes.main_menu_scene import Main_menu_scene
from systems.game_state_manager import Game_state_manager

class Game:
    """Main class responsible only for initializing the game, 
    running the game loop and handling cleanup on exit.
    """
    # Private class constants
    __FPS: int = 60
    __WINDOW_CAPTION: str = "Maze Game"

    def __init__(self):
        """
        Single responsability: initialize the core game infrastructure
        """
        self.__init_pygame()
        self.__init_display()
        self.__init_game_systems()

    def __init_pygame(self) -> None:
        """
        Single responsability: to initialize pygame and it's required modules
        """
        pygame.init()
        if not pygame.get_init():
            raise RuntimeError("Pygame failed to initialize")
        
        if not pygame.font.get_init():
            pygame.font.init()

    def __init_display(self) -> None:
        """
        Single responsability: to initialize display related components:
        - Display resolution
        - Screen
        - Game surface
        - Display caption
        - Display icon
        """
        self.__res = Display_resolution()
        self.__screen = pygame.display.set_mode(
            self.__res.get_game_surf_size(),
            pygame.SCALED | pygame.NOFRAME
        )
        pygame.display.set_caption(self.__WINDOW_CAPTION)
        # TODO:self.ICON = pygame.image.load("PATH")
        # TODO: pygame.display.set_icon(self.ICON)
        self.__game_surface = pygame.Surface(self.__res.get_game_surf_size())

    def __init_game_systems(self) -> None:
        """
        Single responsability: Initialize game management systems and scenes
        """
        self.__game_state_manager = Game_state_manager()
        self.__current_scene = Main_menu_scene(self.__game_surface, self.__game_state_manager)
        self.__clock = pygame.time.Clock()
        self.__running = True
        
    def run(self):
        """
        Single Responsibility: To execute the main game loop
        It should only handle the high-level flow of the game:
        Event handling
        State updates
        Rendering
        Frame rate control
        It shouldn't contain any game logic specifics, which are delegated to the scenes and game manager
        """
        while self.__running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                self.__current_scene.handle_event(event)
            
            # Update game state
            self.__current_scene.update()
            
            # Clear game surface
            self.__game_surface.fill((0, 0, 0))
            
            # Render current scene to game surface
            self.__current_scene.render()
            
            # Scale and blit game surface to screen
            scaled_surface = pygame.transform.scale(
                self.__game_surface, 
                self.__screen.get_size()
            )
            self.__screen.blit(scaled_surface, (0, 0))
            
            # Update display
            pygame.display.flip()
            
            # Cap the frame rate
            self.__clock.tick(self.__FPS)
            
            # Check if game should quit
            if not self.__game_state_manager.get_state("running", True):
                self.__running = False
    
    def cleanup(self):
        """Single Responsibility: To properly release system resources
        (like pygame's resources) that were allocated during the game's execution.  
        """
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.cleanup()