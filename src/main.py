#!/usr/bin/env python3
"""
Main entry point for the Maze Game.
"""
import pygame
import sys
from utils.display_resolution import Display_resolution
from scenes.main_menu_scene import Main_menu_scene
from systems.game_manager import Game_manager

class Game:
    """Main class responsible only for initializing the game, 
    running the game loop and handling cleanup on exit.
    """
    
    def __init__(self):
        # Basic initialization only
        # No game logic here
        pygame.init()
        if not pygame.get_init():
            raise RuntimeError("Pygame failed to initialize")
        
        if not pygame.font.get_init():
            pygame.font.init()
        
        # Creating the window and the game surface that will be blitted to the window
        self.__res = Display_resolution()
        self.__screen = pygame.display.set_mode(
            self.__res.get_game_surf_size(),
            pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME
        )
        pygame.display.set_caption("Maze Game")
        # self.ICON = pygame.image.load("PATH")
        # pygame.display.set_icon(self.ICON)
        self.__game_surface = pygame.Surface(self.__res.get_game_surf_size())

        # Initialize game manager
        self.__game_manager = Game_manager()
        
        # Create initial scene (menu)
        self.__current_scene = Main_menu_scene(self.__game_surface, self.__game_manager)

        self.__clock = pygame.time.Clock()
        self.__running = True
        
    def run(self):
        """Run the main game loop."""
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
            self.__clock.tick(60)
            
            # Check if game should quit
            if not self.__game_manager.get_state("running", True):
                self.__running = False
    
    def cleanup(self):
        """Clean up resources."""
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.cleanup()