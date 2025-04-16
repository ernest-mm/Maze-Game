#!/usr/bin/env python3
"""
Utility class for handling font initialization and management.
"""
import os
import pygame
from typing import Optional

class Font:
    """Utility class for font management."""
    
    # Default font path - can be changed if needed
    DEFAULT_FONT_PATH = os.path.join("assets", "fonts", "default.ttf")
    
    @staticmethod
    def get_font(size: int, font_path: Optional[str] = None) -> pygame.font.Font:
        """
        Get a font with the specified size.
        
        Args:
            size: The size of the font
            font_path: Optional path to a custom font file. If not provided, uses the default font.
            
        Returns:
            pygame.font.Font: The initialized font
            
        Raises:
            FileNotFoundError: If the font file cannot be found
            pygame.error: If the font cannot be initialized
        """
        try:
            # Initialize pygame.font if not already initialized
            if not pygame.font.get_init():
                pygame.font.init()
            
            # Use custom font if provided, otherwise use default
            font_path = font_path or Font.DEFAULT_FONT_PATH
            
            # Check if font file exists
            if not os.path.exists(font_path):
                # If custom font not found, fall back to system font
                return pygame.font.SysFont(None, size)
                
            return pygame.font.Font(font_path, size)
        except pygame.error as e:
            # If there's an error loading the font, fall back to system font
            print(f"Warning: Could not load font {font_path}. Using system font instead. Error: {e}")
            return pygame.font.SysFont(None, size)
    
    @staticmethod
    def set_default_font_path(path: str) -> None:
        """
        Set the default font path.
        
        Args:
            path: The path to the default font file
        """
        Font.DEFAULT_FONT_PATH = path 