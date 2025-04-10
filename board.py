import pygame
import sys

pygame.init()

class Board:
        # Color definitions
    WHITE = (255, 255, 255)
    GREEN = (34, 177, 76)
    BLACK = (0, 0, 0)
    
    def __init__(self, width, height, game_area_rect, ui_area_rect):
        self.width = width
        self.height = height
        self.game_area_rect = game_area_rect
        self.ui_area_rect = ui_area_rect

        # Colors for the areas
        self.background_color = Board.WHITE
        self.game_area_color = Board.GREEN
        self.ui_area_color = Board.BLACK
        
    def draw(self, screen):
        # Background
        screen.fill(self.background_color)
        
        # Draw the game area (e.g., as a green rectangle)
        pygame.draw.rect(screen, self.game_area_color, self.game_area_rect)
        # Draw the UI area (bottom, as a black rectangle)
        pygame.draw.rect(screen, self.ui_area_color, self.ui_area_rect)
        
        # Text in the game area
        font = pygame.font.SysFont(None, 36)
        game_text = font.render("Spielfeld", True, Board.WHITE)
        screen.blit(game_text, (self.game_area_rect.x + 20, self.game_area_rect.y + 20))
        
        # Text in the UI area
        ui_text = font.render("UI Bereich", True, Board.WHITE)
        screen.blit(ui_text, (self.ui_area_rect.x + 20, self.ui_area_rect.y + 20))