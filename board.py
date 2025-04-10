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
        self.tile_image = pygame.image.load("assets/concepts/floor_tile.png").convert()
        self.tile_image = pygame.transform.scale(self.tile_image, (200, 200))

    def draw(self, screen):
        # Draw tile background in the game area
        tile_w, tile_h = self.tile_image.get_size()
        for x in range(self.game_area_rect.left, self.game_area_rect.right, tile_w):
            for y in range(self.game_area_rect.top, self.game_area_rect.bottom, tile_h):
                screen.blit(self.tile_image, (x, y))

        # Draw the UI area (bottom, black rectangle)
        pygame.draw.rect(screen, self.ui_area_color, self.ui_area_rect)

        # Game area text
        font = pygame.font.SysFont(None, 36)
        game_text = font.render("Spielfeld", True, Board.WHITE)
        screen.blit(game_text, (self.game_area_rect.x + 20, self.game_area_rect.y + 20))

        # UI text
        ui_text = font.render("", True, Board.WHITE)
        screen.blit(ui_text, (self.ui_area_rect.x + 20, self.ui_area_rect.y + 20))